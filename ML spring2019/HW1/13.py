# coding: utf-8
#第13題
import numpy as np
from sklearn import svm
import matplotlib.pyplot  as  plt 

train = np.loadtxt('features.train.txt')
test = np.loadtxt('features.test.txt')
train_X = np.array(train[:,1:3])
# ''2'' versus 'not 2' plot |w| versus  logC{-5,-3,-1,1,3}
train_Y = np.array((train[:,0]==2))

c = [-5,-3,-1,1,3]
W = []

for i in c:
    print('C=',i)
    clf = svm.SVC(kernel = "linear",C = 10**i)
    clf.fit(train_X,train_Y)
    w = clf.coef_[0]
    W.append(np.sqrt(np.sum(w*w)))
    print('ok')
    
plt.scatter(c,W)
plt.xlabel('logC')
plt.ylabel('|W|')
plt.savefig("problem13.png")
plt.show()
