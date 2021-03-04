
# coding: utf-8
import numpy as np
import os
import matplotlib.pyplot as plt

def sigmoid(s):
    return 1/(1+np.exp(-s))

def gradient_w(x,y,w):
    g_e_in=0
    for i in range(len(x)):
        g_e_in += sigmoid(np.dot(-y[i]*x[i],w))*(-y[i]*x[i])
    return g_e_in/len(x)

def SGD(x,y,w,i):
    g_e_in = sigmoid(np.dot(-y[i]*x[i],w))*(-y[i]*x[i])
    return g_e_in
    

def sign(s):
    data = []
    for i in range(len(s)):
        if s[i] >= 0.5:
            data.append(1)
        else:
            data.append(-1)
    return np.array(data)

def error(h,true):
    error_rate = 0
    for i in range(len(h)):
        if h[i]!=true[i]:
            error_rate += 1
    return error_rate/len(h)
            
data = np.loadtxt(os.path.join('hw3_train.dat.txt'))
x_train = data[:,0:-1]
y_train = data[:,-1]
data = np.loadtxt(os.path.join('hw3_test.dat.txt'))
x_test = data[:,0:-1]
y_test = data[:,-1]
'''add x0=1'''
x_train = np.concatenate((np.ones((len(x_train),1)),x_train),axis=1)
x_test = np.concatenate((np.ones((len(x_test),1)),x_test),axis=1)
"initialization"
l_rate19 = 0.01
l_rate20 = 0.001
iteration = 2000
w = np.zeros(21)
SGD_w = np.zeros(21)
error_rate = []
E_out_error = []
index = []
"star training"
for i_ter in range(iteration):
    
    "Gradient descent start"
    E_in = sign(sigmoid(np.dot(x_train,w)))
    E_out = sign(sigmoid(np.dot(x_test,w)))
    grad_w = gradient_w(x_train,y_train,w)
    w = w - l_rate19*grad_w
    #if i_ter%1==0 or i_ter==(iteration-1):
    error_rate.append([error(E_in,y_train)])
    E_out_error.append([error(E_out,y_test)])
    
    "Stochastic Gradient Descent start"
    E_in = sign(sigmoid(np.dot(x_train,SGD_w)))
    E_out = sign(sigmoid(np.dot(x_test,SGD_w)))
    grad_w = SGD(x_train,y_train,SGD_w,i_ter%len(x_train))
    SGD_w = SGD_w - l_rate20*grad_w
    #if i_ter%1==0 or i_ter==(iteration-1):
    index.append(i_ter)
    error_rate[len(error_rate)-1].append(error(E_in,y_train))
    E_out_error[len(error_rate)-1].append(error(E_out,y_test))
    print("iteration = %d | (gd,SGD) error rate = (%3f,%3f)" %(i_ter,error_rate[len(error_rate)-1][0],error_rate[len(error_rate)-1][1]))

error_rate=np.array(error_rate)
E_out_error=np.array(E_out_error)
index=np.array(index)
"Plot E_in"
plt.plot(index,error_rate[:,0],"r",label="GD l_rate=0.01")
plt.plot(index,error_rate[:,1],"b",label="SGD l_rate=0.001")
plt.xlabel('E_in with GD & SGD')
plt.ylabel('Error rate')
plt.title('Problem 4')
plt.legend()
plt.savefig('Problem4.png')
plt.show()
"Plot E_out"
plt.plot(index,E_out_error[:,0],"r",label="GD l_rate=0.01")
plt.plot(index,E_out_error[:,1],"b",label="SGD l_rate=0.001")
plt.xlabel('E_out with GD & SGD')
plt.ylabel('Error rate')
plt.title('Problem 5')
plt.legend()
plt.savefig('Problem5.png')
plt.show()

