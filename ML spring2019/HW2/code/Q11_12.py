
# coding: utf-8
#Q11,Q12
import numpy as np

data = np.loadtxt('hw2_lssvm_all.dat.txt')
train_x = np.concatenate((np.ones((500,1)),data[:,:-1]),axis=1)[0:400]
train_y = np.array(data[0:400,-1])
test_x = np.concatenate((np.ones((500,1)),data[:,:-1]),axis=1)[400:]
test_y = np.array(data[400:,-1])
Lambda = [0.05,0.5,5,50,500]
g_train = np.zeros((len(Lambda),train_y.shape[0]))
g_test = np.zeros((len(Lambda),test_y.shape[0]))
E_in = []
E_out = []
#not repeat data
"""
for seed in range(250):
    np.random.seed(seed+1120)
    new_data = np.random.shuffle(data)
    bootstrapped_x = np.concatenate((np.ones((500,1)),data[:,:-1]),axis=1)[0:400]
    bootstrapped_y = np.array(data[0:400,-1])
    for index in range(len(Lambda)):
        i = Lambda[index]
        w = np.dot(np.dot(np.linalg.inv(i*np.identity(bootstrapped_x.shape[1])+np.dot(np.transpose(bootstrapped_x),
                                        bootstrapped_x)),np.transpose(bootstrapped_x)),bootstrapped_y)
        train_result = np.sign(np.dot(w,np.transpose(train_x)))
        g_train[index] += train_result
        test_result = np.sign(np.dot(w,np.transpose(test_x)))
        g_test[index] += test_result
g_train = np.sign(g_train)
g_test = np.sign(g_test)
for i in g_train:
    ein = np.mean(i != train_y)
    E_in.append(ein)
for i in g_test:
    eout = np.mean(i != test_y)
    E_out.append(eout)
print("E in =",E_in)
print("E out=",E_out)
"""
#隨機取可重複
np.random.seed()
for iter in range(250):
    bootstrapped_x = []
    bootstrapped_y = []
    for i in range(400):
        random = np.random.randint(low=0,high=400)
        bootstrapped_x.append(train_x[random])
        bootstrapped_y.append(train_y[random])
    bootstrapped_x=np.array(bootstrapped_x)
    bootstrapped_y=np.array(bootstrapped_y)
    for index in range(len(Lambda)):
        i = Lambda[index]
        w = np.dot(np.dot(np.linalg.inv(i*np.identity(bootstrapped_x.shape[1])+np.dot(np.transpose(bootstrapped_x),
                                        bootstrapped_x)),np.transpose(bootstrapped_x)),bootstrapped_y)
        train_result = np.sign(np.dot(w,np.transpose(train_x)))
        g_train[index] += train_result
        test_result = np.sign(np.dot(w,np.transpose(test_x)))
        g_test[index] += test_result
g_train = np.sign(g_train)
g_test = np.sign(g_test)
for i in g_train:
    ein = np.mean(i != train_y)
    E_in.append(ein)
for i in g_test:
    eout = np.mean(i != test_y)
    E_out.append(eout)
print("E in =",E_in)
print("E out=",E_out)