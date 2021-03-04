import numpy as np
import sys

"""
Inputs: 
(1) S (spot price)
(2) X (strike price)
(3) H (barrier price)
(4) T (years)
(5) r (risk-free interest rate)
(6) s (volatility)
(7) n (number of periods)
(8) k (number of simulation paths) 

Output: 
(1)put price 
(2)standard error
(3)delta

#least-squares Monte Carlo program to price up-and-out American-style Asian puts
"""

S = float(sys.argv[1])
X = float(sys.argv[2])
H = float(sys.argv[3])
T = float(sys.argv[4])
r = float(sys.argv[5])
s = float(sys.argv[6])
n = int(sys.argv[7])
k = int(sys.argv[8])

def MOTECOROW(S,X,H,T,r,s,n,k):
    delT = T/n
    price = S
    Monte_price = np.zeros((k, n))
    epsilon = np.random.normal(loc=0, scale=1,size=k)
    Monte_price[:,0] = price * np.exp((r - (s**2)/2)*delT + s*(np.sqrt(delT))*epsilon)
    for i in range(1,n):
        print("Monte price:",i)
        epsilon = np.random.normal(loc=0, scale=1,size=k)
        Monte_price[:,i] = Monte_price[:,i-1] * np.exp((r - (s**2)/2)*delT + s*(np.sqrt(delT))*epsilon)
    print("========== Monte price finished ==========")
    #Asian求mean
    mean_price = np.zeros((k, n))
    for i in range(n):
        print("mean:",i)
        mean_price[:,i] = np.mean(Monte_price[:,:i+1],axis=1)
    print("========== Mean price finished ==========")
    #判斷誤差
    diff = np.maximum(0,X - mean_price)
    original_mean_price = mean_price.copy()
    mean_price[diff==0]=0
    Cost = np.concatenate( (np.zeros((k,n-1)),(diff[:,-1]*np.exp(-r*delT)).reshape(-1,1) ),axis=1)
    #求Hit
    Hit = (original_mean_price>H)
    Cost[:,-1] *= (~Hit[:,-1]).astype(int)
    cal_Hit = np.zeros(k)
    
    #iteration
    for i in range(n-2, -1, -1):
        print("Cost:",i)
        degree = 5
        reg1 = np.polyfit(mean_price[:, i], Cost[:, i + 1], degree)
        regression = np.poly1d(reg1)
        payoff = regression(mean_price[:,i])

        #更新 payoff 及 difference
        temp = (payoff > (diff[:,i]) ).astype(int)
        Cost[:,i] = temp*Cost[:, i + 1]*np.exp(-r*delT)
        temp = (payoff <= (diff[:,i])).astype(int)
        Cost[:,i] += temp*diff[:,i]*np.exp(-r*delT)
        #Hit為0就為0
        cal_Hit += Hit[:,i]
        Cost[cal_Hit>0,i]=0
        #Cost[:,i] *= Hit[:,i]
    print("========== Cost price finished ==========")
    PRICE = np.mean(Cost[:,0])
    STD = np.std(Cost[:,0])/np.sqrt(k)

    return PRICE,STD

if __name__ == '__main__':
    mid_PRICE,mid_STD = MOTECOROW(S,X,H,T,r,s,n,k)
    up_PRICE,up_STD = MOTECOROW(S*1.01,X,H,T,r,s,n,k)
    down_PRICE,down_STD = MOTECOROW(S*0.99,X,H,T,r,s,n,k)
    delta = (up_PRICE-down_PRICE)/(S*0.02)
    print("put price {}\nstandard error {}\n".format(mid_PRICE,mid_STD))
    print("delta {}".format(delta))
    #put price 5.4310
    #standard error 0.0085
    #delta  -0.4122