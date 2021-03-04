# coding: utf-8
#第14題
import numpy as np
from sklearn import svm
import matplotlib.pyplot  as  plt 

train = np.loadtxt('features.train.txt')
test = np.loadtxt('features.test.txt')
train_X = train[:,1:3]
train_Y = []
# ''4'' versus 'not 4' logC{-5,-3,-1,1,3}
train_Y = np.array((train[:,0]==4))
        
c = [-5,-3,-1,1,3]
E_in = []

for i in c:
    clf = svm.SVC(kernel = "poly",C = 10**i,degree=2,coef0 = 1,gamma=1)
    print("c=",i)
    clf.fit(train_X,train_Y)
    print('Ok')
    error = np.sum(clf.predict(train_X) !=train_Y)/len(train_X)
    E_in.append(error)
    
plt.scatter(c,E_in)
plt.xlabel('logC')
plt.ylabel('E_in')
plt.savefig("problem14_E_in.png")
plt.show()
