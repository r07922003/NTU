# coding: utf-8
#Q9,Q10
import numpy as np

data = np.loadtxt('hw2_lssvm_all.dat.txt')
train_x = np.concatenate((np.ones((500,1)),data[:,:-1]),axis=1)[0:400]
train_y = np.array(data[0:400,-1])
test_x = np.concatenate((np.ones((500,1)),data[:,:-1]),axis=1)[400:]
test_y = np.array(data[400:,-1])
Lambda = [0.05,0.5,5,50,500]
E_in = []
E_out = []
for i in Lambda:
    w = np.dot(np.dot(np.linalg.inv(i*np.identity(train_x.shape[1])+np.dot(np.transpose(train_x),train_x)),np.transpose(train_x)),train_y)
    train_result = np.sign(np.dot(w,np.transpose(train_x)))
    test_result = np.sign(np.dot(w,np.transpose(test_x)))
    ein = np.mean(train_result != train_y)
    eout = np.mean(test_result != test_y)
    E_in.append(ein)
    E_out.append(eout)
print("E in =",E_in)
print("E out=",E_out)