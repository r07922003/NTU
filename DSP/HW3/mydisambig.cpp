#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <stdio.h>
#include <vector>
#include "Ngram.h"
using namespace std ;

FILE *open_or_die( const char *filename, const char *ht )
{
   FILE *fp = fopen( filename, ht );
   if( fp == NULL ){
      perror(filename);
      exit(1);
   }
   return fp;
}

// Get P(W2 | W1) -- bigram
double getBigramProb(const char *w1, const char *w2, Vocab &voc , Ngram &lm)
{
    VocabIndex wid1 = voc.getIndex(w1);
    VocabIndex wid2 = voc.getIndex(w2);
    if (strcmp(w1, "<unk>") == 0){
        wid1 = Vocab_None;
    }
    if(wid1 == Vocab_None)  //OOV
        wid1 = voc.getIndex(Vocab_Unknown);
    if(wid2 == Vocab_None)  //OOV
        wid2 = voc.getIndex(Vocab_Unknown);

    VocabIndex context[] = { wid1, Vocab_None };
    return lm.wordProb( wid2, context);
}

int main(int argc, char *argv[])
{
    VocabIndex viterbi_map[8700][87];
    int ch_0 = -93; // 注音的ch[0]
    int ch_1[37] = {116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -72, -71, -70, -85, -84, -83, -82, -81, -80, -79, -78, -77, -76, -75, -74, -73};
    vector<string> mapTable[37]; // save[八 匕 卜 不 卞 巴 比 丙 包 北 半 叭 布...]...
    
    //cmd: ./mydisambig -text testdata/$$i.txt -map $(TO) -lm $(LM) -order 2  result2/$$i.txt
    char *test_name = argv[2];  //get test file arguments
    char* map_name = argv[4];   //get map file arguments 
    char* lm_name = argv[6];    //get lm file arguments 
    int order = atoi(argv[8]);  //get order num
    char* out_name =argv[9];         //get output file arguments

    ifstream file(test_name);   //開啟testdata
    ifstream map(map_name);     //開啟mapdata
    ofstream out(out_name);
    //ofstream out("output.txt"); //debug用 

    char ch[2];                 //宣告國字兩個char
    string str;
    string cancel;
//get ㄅ [八 匕 卜 不 卞 巴 比 丙 包 北 半 叭 布...] ㄅ後面的那些字------------------------------------------
    while(map >> ch){
        /*注音 int(ch[0])皆是-93  ch[1] 注音對照如下:
        ㄅ   ㄆ  ㄇ  ㄈ  ㄉ  ㄊ  ㄋ   ㄌ  ㄍ  ㄎ   ㄏ  ㄐ  ㄑ  ㄒ  ㄓ   ㄔ  ㄕ  ㄖ   ㄗ  ㄘ  ㄙ  ㄧ  ㄨ  ㄩ  ㄚ  ㄛ   ㄜ  ㄝ  ㄞ  ㄟ  ㄠ   ㄡ ㄢ   ㄣ  ㄤ  ㄥ   ㄦ
        116 117 118 119 120 121 122 123 124 125 126 -95 -94 -93 -92 -91 -90 -89 -88 -87 -86 -72 -71 -70 -85 -84 -83 -82 -81 -80 -79 -78 -77 -76 -75 -74 -73*/
        //cout <<int(ch[0]) <<"  " <<int(ch[1]) <<endl;
        
        if (int(ch[0]) == ch_0){
            for (int i=0; i<37; i++){
                if ((int)ch[1] == ch_1[i]){
                    getline(map,str);
                    istringstream sss(str);
                    string temp;
                    while(sss >> temp){
                        mapTable[i].push_back(temp);
                    }
                    break;
                }
            }
        }
        else{
            getline(map,cancel);
        }
    }
/*
    debug//印出map
    for(int i=0;i<37;i++){
        for(int j=0;j <mapTable[i].size();j++){
            out <<mapTable[i][j];
        }
        out <<endl;
    }
*/
    map.close();
//-map 結束-------------------------------------------------------------------------------------------------------
    Vocab voc;
    Ngram lm( voc, order );
    {
        File lmFile( lm_name, "r" );
        lm.read(lmFile);
        lmFile.close();
    }
//------------------------------------------------------------------------------------------------------------------
    char tmp[1000];
    char *nowWord;
    while(file.getline(tmp, sizeof(tmp))){
        istringstream sss(tmp);
        string temp;
        out <<"<s> ";
        while(sss >> temp){
            if(int(temp[0])==ch_0 ){
                for (int i=0; i<37; i++){
                    if ((int)temp[1] == ch_1[i]){
                        out << mapTable[i][0] <<" ";
                    }
                }
            }
            else{
                out <<temp <<" ";
            }
        }
        /*
        for(int i=0;i<sizeof(tmp);i++){
            if(i==0){
                out <<"<s> ";
            }
            if(tmp[i] != ' ' && tmp[i+1] != ' '){
                if(int(tmp[i])==ch_0 ){
                    for (int j=0; j<37; j++){
                        if ((int)tmp[i+1] == ch_1[j]){
                            out << mapTable[j][0] <<" ";
                        }
                    }
                }
            }
        }
        */
        out <<"</s>" <<endl;
    }
}
