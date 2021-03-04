
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

def sign(x):
    data = []
    for i in x:
        if i>=0:
            data.append(1)
        else:
            data.append(-1)
    return data

def s_head(x,noise):
    temp=sign(np.random.uniform(low = 0.0,high = 1.0,size = 20)-noise) #隨機生成[0,1]之間的序列扣掉noise%數實現noise data
    array = sign(x)
    return np.array(temp)*np.array(array)

def get_seeda(x): #因為要算E_out所以需要seeda正確的值
    data=[]
    data_size = len(x)
    x = np.sort(x)
    for i in range(data_size-1):
        data.append( (x[i]+x[i+1])/2 )
    data.append(1.0)
    return data

def h(s,x,seeda,true_noise_y):
    error = []
    num = 0
    for i in range(len(seeda)):
        count = 0
        temp = s*np.array(sign(x-seeda[i])) 
        #計算 temp 跟 true_noise_y 的error
        for j in (temp+true_noise_y):
            if j==0:
                count += 1
            #print(temp)
            #print(true_noise_y)
            #print(temp + true_noise_y)
        error.append(count/20)
    for i in range(len(error)):
        if error[i] == min(error):
            num = i
            break
    return (min(error),seeda[num])


iteration = 1000
sub = []
for i in range(iteration):
    #hypothes = s * sign(x-seeda)   
    x = np.array( np.random.uniform(low = -1.0,high = 1.0,size = 20) ) #產生x的data
    true_noise_y = np.array(s_head(x,0.2)) #產生true_noise_y的data
    seeda = get_seeda(x) #依照x的資料去生成data中間數的間隔點
    e_in = np.zeros((2,2))
    e_in[0][0],e_in[0][1] = h(1,x,seeda,true_noise_y) #s = 1
    e_in[1][0],e_in[1][1] = h(-1,x,seeda,true_noise_y) #s = -1

    if e_in[0][0] < e_in[1][0]:
        s = 1
        E_in = e_in[0][0] #get E_in
        best_seeda = e_in[0][1]
    else:
        s = -1
        E_in = e_in[1][0] #get E_in
        best_seeda = e_in[1][1]
    E_out = 0.5 + 0.3*s*(np.abs(best_seeda)-1) #根據第六題算出來的E_out
    sub.append(E_in-E_out)
plt.hist(sub,bins=30,facecolor='red', alpha=0.5)
plt.xlabel('E_in - E_out')
plt.ylabel('Count')
plt.title('Problem 7')
plt.savefig('E_in-E_out')
plt.show()

