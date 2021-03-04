# coding: utf-8
#第15題
import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt 

train = np.loadtxt('features.train.txt')
test = np.loadtxt('features.test.txt')
train_X = train[:,1:3]
train_Y = []
# ''0'' versus 'not 0' logC{-2,-1,0,1,2}
train_Y = np.array((train[:,0]==0))

c = [-2,-1,0,1,2]
distance = []

for i in c:
    clf = svm.SVC(kernel = 'rbf',gamma = 80,C = 10**i)
    clf.fit(train_X,train_Y)
    w = clf.dual_coef_[0].dot(clf.support_vectors_)
    dis = 1/np.sum(w*w)
    distance.append(dis)

plt.scatter(c,distance)
plt.xlabel('logC')
plt.ylabel('distance')
plt.savefig("problem15_distance.png")
plt.show()
