import os

f = open(os.path.join('Big5-ZhuYin.map'),encoding='big5-HKSCS',mode='r')
dict={'ㄅ':[],'ㄆ':[],'ㄇ':[],'ㄈ':[],'ㄉ':[],'ㄊ':[],'ㄋ':[],'ㄌ':[],'ㄍ':[],'ㄎ':[],'ㄏ':[],'ㄐ':[],'ㄑ':[],'ㄒ':[],'ㄓ':[],'ㄔ':[],'ㄕ':[],'ㄖ':[],'ㄗ':[],'ㄘ':[],'ㄙ':[],'ㄧ':[],'ㄨ':[],'ㄩ':[],'ㄚ':[],'ㄛ':[],'ㄜ':[]
        ,'ㄝ':[],'ㄞ':[],'ㄟ':[],'ㄠ':[],'ㄡ':[],'ㄢ':[],'ㄣ':[],'ㄤ':[],'ㄥ':[],'ㄦ':[]}
lines=f.readlines()

f.close()
for i in range(len(lines)):
    c = lines[i].split(' ')
    a = c[1].split('/')
    for j in range(len(a)):
        if c[0] not in dict[a[j][0]]:
            dict[a[j][0]].append(c[0])

w = open(os.path.join('ZhuYin-Big5.map'),encoding='big5-HKSCS', mode='w+')
for i in dict:
    w.write(i+'\t')
    for j in dict[i]:
        w.write(j+" ")
    w.write("\n")
    for j in dict[i]:
        w.write(j+'\t'+j+'\n')
w.close()
