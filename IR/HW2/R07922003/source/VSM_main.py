
# coding: utf-8

# In[16]:


import numpy as np
import xml.etree.cElementTree as ET
import csv
from argparse import ArgumentParser

#Okipi/BM25 Parmeters
BM25_k = 0.71
BM25_b = 0.21

#Rocchio Feedback parameters
alpha = 0.8
beta = 0.3
gamma = 0.5
ratio = 0.02

def read_voc(model_dir):
    file = open(str(model_dir)+'/vocab.all','r',encoding='utf8')
    voc = []
    for i in file:
        voc.append(i)
        voc[-1] = i.split('\n')[0]
    file.close()
    return voc

def read_file_list(model_dir,Doc_path):
    file = open(str(model_dir)+"/file-list",'r')
    file_list = []
    Avg_file_length = 0
    print('----->Reading File List----->')
    for i in file:
        filename=i.split('\n')[0]
        Documet = open(str(Doc_path)+'/'+filename,'r',encoding='utf8')
        Doc_info = {}
        tree = ET.parse(Documet)
        root = tree.getroot()
        Doc_info['id'] = root.findtext('doc/id').lower()
        Doc_info['date'] = root.findtext('doc/date').lower()
        try:
            root.findtext('doc/title')
        except:
            Doc_info['title'] = ''
        else:
            Doc_info['title'] = root.findtext('doc/title').strip(' ')
        Doc_info['content']=''
        for p in root.iter('p'):
            Doc_info['content'] += p.text.strip()
        file_list.append(Doc_info)
    for doc in file_list:
        Avg_file_length += len(doc['content'])
    Avg_file_length = float(Avg_file_length/len(file_list))
    print('Average Doc Length: ' + str(Avg_file_length))
    file.close()
    return file_list,Avg_file_length

def read_inverted_file(model_dir):
    InvertedFileDict = {}
    currentIndex = ""
    print('----->Reading Inverted List----->')
    with open(str(model_dir) + '/inverted-file') as f :
        Invert = [line.rstrip('\n') for line in f]
        for i,info in enumerate(Invert):
            fields = info.split(' ')
            if len(fields)==3:
                if fields[1] == '-1':  #unigram
                    currentIndex = str(fields[0]+',-1')
                    for n in range(int(fields[2])):
                        (DocId,CountInDoc) = Invert[i+n+1].split(' ')
                        try:
                            InvertedFileDict[currentIndex]
                        except:
                            #not exist index
                            InvertedFileDict[currentIndex] = {'Doc_Freq': fields[2] ,'Docs':[]}
                        else:
                            pass
                        finally:
                            InvertedFileDict[currentIndex]['Docs'].append({'DocID':DocId,'CountInDoc':CountInDoc})
                else:  #bigram
                    currentIndex = str(fields[0]+','+fields[1])
                    for n in range(int(fields[2])):
                        (DocId,CountInDoc) = Invert[i+n+1].split(' ')
                        try:
                            InvertedFileDict[currentIndex]
                        except: 
                            #not exist index
                            InvertedFileDict[currentIndex] = {'Doc_Freq': fields[2],'Docs':[]}
                        else:
                            pass
                        finally:
                            InvertedFileDict[currentIndex]['Docs'].append({'DocID':DocId,'CountInDoc':CountInDoc})
            else:
                pass
    #print(len(InvertedFileDict))
    return InvertedFileDict

def Bigram_Query(query):
    with open(str(query)) as f:
        print("Reading Query ---> "+query)
        tree = ET.parse(query)
        root = tree.getroot()
        queryTerm = {}
        queryId = []
        for topic in root.iter('topic'):
            query_id = topic.findtext('number')[-3:].strip() #只取Doc末3碼
            queryId.append(query_id)
            queryTerm[query_id] = {}
            title = topic.findtext('title').strip()
            concepts = topic.findtext('concepts').strip()
            
            puncs = [u'，', u'?', u'@', u'!', u'$', u'%', u'『', u'』', u'「', u'」', u'＼', u'｜', u'？', u' ', u'*', u'(', u')', u'~', u'.', u'[', u']', 'u\n',u'1',u'2',u'3',u'4',u'5',u'6',u'7',u'8',u'9',u'0', u'。']
            #字串前面 + u 為unicode編碼表示
            for punc in puncs:
                #消除puncs
                concepts = concepts.replace(punc,'')
            #開始處理xml檔裡的concepts
            for term in concepts.split(u'、'):
                if len(term)%2==0:    #偶數的詞用 2 個 shift window
                    for i in range(0,len(term),2):
                        try:
                            queryTerm[query_id][term[i]+term[i+1]]
                        except: #first
                            queryTerm[query_id][term[i]+term[i+1]] = 1
                        else:
                            queryTerm[query_id][term[i]+term[i+1]] += 1
                else:      #奇數的詞用 1 個 shift window
                    for i in range(0,len(term)-1,1):
                        try:
                            queryTerm[query_id][term[i]+term[i+1]]
                        except: #first
                            queryTerm[query_id][term[i]+term[i+1]] = 1
                        else:
                            queryTerm[query_id][term[i]+term[i+1]] += 1
    return queryTerm,queryId

def VSM(queryTerm,queryId,queryNum,Voc,InvertedFileDict,File_list,Avg_Doc_Len):
    queryVector=[]
    ranking = {}
    queryTermsIndex = 0
    print('len(queryTerm):',len(queryTerm[queryId[queryNum]]))
    for key, freq in queryTerm[queryId[queryNum]].items():
        print(key,freq)
        if key[0] in Voc:
            if key[1] in Voc:
                key0 = str(Voc.index(key[0]))
                key1 = str(Voc.index(key[1]))
                Inverted_Idex = key0 + ',' + key1
                if Inverted_Idex in InvertedFileDict:
                    #Okapi/BM25
                    queryVector.append(freq) #Query Vector
                    BigramDoc = InvertedFileDict[Inverted_Idex]
                    Doc_Freq = int(BigramDoc['Doc_Freq'])
                    Docs = BigramDoc['Docs']

                    # IDF(w) = log(m+1/k)    m=total number of docsm      k=numbers of docs with term t (doc freq)
                    m = len(File_list)
                    k = Doc_Freq
                    IDF = np.log( (m+1)/k )
                    #print(IDF)
                    
                    #TF(t,d) = (k+1) * count(t,d) / (count(t,d)+k)    k>=0
                    
                    for doc in Docs:
                        DocID = int(doc['DocID'])
                        DocLen = len(File_list[DocID]['content'])   
                        CountInDoc = int(doc['CountInDoc'])
                        #Pivot BM25/Okapi TF(t,d) = (k+1)*count(t,d) / (count(t,d) + k(1−b+ b * |d| / Avg_Doc_Len ))
                        #TF = (BM25_k + 1)*CountInDoc / (CountInDoc + BM25_k*(1 - BM25_b + BM25_b* DocLen / Avg_Doc_Len))
                        #Pivoted Length Normalization VSM ln[1+ln[1+c(w,d)]] / (1−b+b * |d| / avdl)
                        TF = np.log(1 + np.log(1+CountInDoc) ) / (1 - BM25_b + BM25_b* DocLen /Avg_Doc_Len)
                        if DocID not in ranking:
                            ranking[DocID] = [0.] *len(queryTerm[queryId[queryNum]])
                        ranking[DocID][queryTermsIndex] = IDF * TF
                    queryTermsIndex += 1
                
                else:
                    queryVector.append(freq)
                    queryTermsIndex += 1
                
                
    return ranking,queryVector

def Rocchio_Feback(queryVector,ranking):
    print('----->Rocchio Feedback')
    rankLength = len(ranking)
    RelevanceCount = int(rankLength * ratio) #取前幾%的當作相關文檔
    
    Score_Dict = {}

    for ID in ranking:
        Score_Dict[ID] = sum(ranking[ID])
    rocchio_Dict = sorted(Score_Dict.items(),key = lambda Score_Dict:Score_Dict[1],reverse = True)
    
    Cr = np.array([0.]*len(queryVector))
    Cnr = np.array([0.]*len(queryVector))
    RelevanceFile = rocchio_Dict[0:RelevanceCount]
    NonRelevanceFile = rocchio_Dict[RelevanceCount:-1]
    
    for ID,Score in RelevanceFile:
        Cr += ranking[ID]
    for ID,Score in NonRelevanceFile:
        Cnr += ranking[ID]
                       
    Optimal_query = (alpha * np.array(queryVector)) + (beta * Cr / RelevanceCount) - (gamma * Cnr / (rankLength-RelevanceCount))
    return Optimal_query
    
        
def Score_result(queryVector,ranking):
    Score_Dict = {}
    for docID,value in ranking.items():
        score = np.dot(value,queryVector)
        Score_Dict[docID] = score 
    result = sorted(Score_Dict.items(),key = lambda Score_Dict:Score_Dict[1],reverse = True)
    return result

def main():
    parser = ArgumentParser()
    parser.add_argument('-r',help="If specified, turn on relevance feedback",action="store_true",default=False)
    parser.add_argument('-b',help="If specified, run best version",action="store_true",default=False)
    parser.add_argument('-i',help="The input query file",type=str)
    parser.add_argument('-o',help="The output ranked list file",type=str)
    parser.add_argument('-m',help="model-dir",type=str)
    parser.add_argument('-d',help="NTCIR-dir",type=str)
    args = parser.parse_args()
    
    File_list,Avg_Doc_Len = read_file_list(args.m,args.d)
    InvertedFileDict = read_inverted_file(args.m)
    Voc = read_voc(args.m)
    
    query_Term,query_Id = Bigram_Query(args.i)
    
    output_name = str(args.o) + '.csv'
    output = open(output_name,'w+')
    s = csv.writer(output,delimiter=',',lineterminator='\n') #lineterminator='\n' 加入此行可使寫入連續不會空一行 
    s.writerow(["query_id","retrieved_docs"])
    
    for index in range(len(query_Id)): 
        ranking,queryVector = VSM(query_Term,query_Id,index,Voc,InvertedFileDict,File_list,Avg_Doc_Len)
        if(args.r):
            queryVector = Rocchio_Feback(queryVector,ranking)
        result = Score_result(queryVector,ranking)
        txt=""
        for i in range(100):
            if i != 99:
                txt += File_list[result[i][0]]['id'] + ' '
            else:
                txt += File_list[result[i][0]]['id']     
        s.writerow([str(query_Id[index]),txt])
    output.close()

if __name__ == "__main__":
    main()

