
# coding: utf-8

from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np

def Histogram_Equalization(coulmn,row,pix):
    total=0
    hist = np.zeros(256)
    S_k = np.zeros(256)
    count = np.zeros(256)
    n = coulmn*row
    for i in range(coulmn):
        for j in range(row):
            hist[pix[i,j]]+=1
    for k in range(256):
        total+=hist[k]
        S_k[k] = (255*(total/n))
    for i in range(coulmn):
        for j in range(row):
            k=int(S_k[pix[i,j]])
            lena.putpixel( (i,j),k )
    for i in range(coulmn):
        for j in range(row):
            count[int(S_k[pix[i,j]])]+=1
    #plt.fill(count,color='black')
    plt.fill_between(np.arange(0,256,1), 0, count,color ='black')
    plt.savefig('Histogram_Equalization.jpg')
    plt.show()
    return lena
lena= Image.open("lena.bmp")
pix=lena.load()
coulmn,row=lena.size
Histogram_Equalization(coulmn,row,pix)

