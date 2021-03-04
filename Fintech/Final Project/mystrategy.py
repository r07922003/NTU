# coding: utf-8
 
def myStrategy(dailyOhlcvFile,minutelyOhlcvFile,openPrice):
    import numpy as np
    price = dailyOhlcvFile['open'].values
    currPrice = openPrice
    dataLen = len(price)
    windowSize = 11
    param=[6,19]
    alpha=param[0]
    beta=param[1]
    action=0
    dataLen = len(price)
    if dataLen<windowSize:
        ma=np.mean(price)
        return 0
    windowedData=price[-windowSize:]
 
    ma=np.mean(windowedData)
    if (currPrice-alpha)>ma:
        action=1
    elif (currPrice+beta)<ma:
        action=-1
    else:
        action=0
 
    n1 = 8 #短期RSI
    n2 = 20 #長期RSI
    RSn1 = np.zeros((2,2))
    RSn2 = np.zeros((2,2))
    RSIn1 = np.zeros(2)
    RSIn2 = np.zeros(2)
    for i in range(dataLen-1,dataLen-n1,-1):
        difference1 = price[i] - price[i-1]
        if difference1 > 0:
            RSn1[0][0] += difference1
        else:
            RSn1[1][0] -= difference1
        difference2 = price[i-1] - price[i-2]
        if difference2 > 0:
            RSn1[0][1] += difference2
        else:
            RSn1[1][1] -= difference2
    RSIn1[0] = 100* (RSn1[0][0]/RSn1[1][0])/(1+(RSn1[0][0]/RSn1[1][0]) ) #今日的 RSI
    RSIn1[1] = 100* (RSn1[0][1]/RSn1[1][1])/(1+(RSn1[0][1]/RSn1[1][1]) ) #昨日的 RSI
 
    for i in range(dataLen-1,dataLen-n2,-1):
        difference1 = price[i] - price[i-1]
        if difference1 > 0:
            RSn2[0][0] += difference1
        else:
            RSn2[1][0] -= difference1
        difference2 = price[i-1] - price[i-2]
        if difference2 > 0:
            RSn2[0][1] += difference2
        else:
            RSn2[1][1] -= difference2
    RSIn2[0] = 100* (RSn2[0][0]/RSn2[1][0])/(1+(RSn2[0][0]/RSn2[1][0]) )
    RSIn2[1] = 100* (RSn2[0][1]/RSn2[1][1])/(1+(RSn2[0][1]/RSn2[1][1]) )
 
    if (RSIn1[0] >=80) or (RSIn2[0] >= 80): #RIS超過80要開始跌了開始賣
        action = -1
    if (RSIn1[0] <=20) or (RSIn2[0] <= 20): #RIS低過20要開始漲了開始買
        action = 1
    if (RSIn1[1] < RSIn2[1]) and (RSIn1[0] > RSIn2[0]): #黃金交叉
        action = 1
    if (RSIn1[0] > RSIn2[0]) and (RSIn1[0] < RSIn2[0]): #死亡交叉
        action = -1
    return action
