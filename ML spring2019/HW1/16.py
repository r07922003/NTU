# coding: utf-8
#第16題
import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt 

def shuffle(X,Y,seed):
    #radom seed to arrange array
    randomize = np.arange(len(X))
    np.random.seed(seed)
    np.random.shuffle(randomize)
    return (X[randomize], Y[randomize])


train = np.loadtxt('features.train.txt')
test = np.loadtxt('features.test.txt')
train_X = train[:,1:3]
train_Y = []

# ''0'' versus 'not 0' C=0.1 log(gamma)={-2,-1,0,1,2}
train_Y = np.array((train[:,0]==0))
test_Y = np.array((test[:,0]==0))

c = 0.1
count = np.zeros(5)
gamma = [-2,-1,0,1,2]

for n in range(100):
    print(n)
    train_x,train_y = shuffle(train_X,train_Y,n+100)
    val_x,val_y=train_x[0:1000],train_y[0:1000]
    x,y = train_x[1000:-1],train_y[1000:-1]
    E_val = []
    
    for i in gamma:
        clf = svm.SVC(kernel='rbf',gamma=10**i,C = c)
        clf.fit(train_X,train_Y)
        e = np.sum(clf.predict(val_x) != val_y)/len(val_x)
        E_val.append(e)
    count[np.argmin(E_val)] += 1

print(count)
plt.bar(gamma,count)
plt.xlabel('gamma')
plt.ylabel('count')
plt.savefig("problem16")
plt.show()
