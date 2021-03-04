def myOptimAction(priceVec, transFeeRate):
    import numpy as np
    import operator
    import sys
    dataLen = len(priceVec)
    actionVec = np.zeros(dataLen)
    spreadVec = np.zeros(dataLen)
    buyPrice = np.zeros(dataLen)
    sellPrice = np.zeros(dataLen)
    buy_sell_mat = np.zeros((dataLen,dataLen))
    conCount = 3
    holdPrice = 0
    sys.setrecursionlimit(1000000)

#    for i in range(dataLen):
#        buyPrice[i] = priceVec[i] * (1+transFeeRate)
#        sellPrice[i] = priceVec[i] * (1-transFeeRate)
#
#    for i in range(-1,dataLen-1):
#        if i == -1:
#            spreadVec[i+1] = 0
#        else:
#            spreadVec[i+1] = priceVec[i+1] - priceVec[i]
#    for i in range(dataLen-1):
#        if spreadVec[i] >= 0 and spreadVec[i+1] > 0:
#            actionVec[i] = 0
#        if spreadVec[i] >= 0 and spreadVec[i+1] <= 0:
#            for j in range(i+1,dataLen-1):
#                if spreadVec[j] > 0:
#                    if sellPrice[i] > buyPrice[j-1]:
#                        actionVec[i] = -1
#                    break
#        elif spreadVec[i] <= 0 and spreadVec[i+1] >= 0:
#            for j in range(i+1,dataLen-1):
#                if spreadVec[j] < 0:
#                    if buyPrice[i] < sellPrice[j-1]:
#                        actionVec[i] = 1
#                    break
#    return actionVec


    ownStock = np.zeros((dataLen, 3))
    unownStock = np.zeros((dataLen, 2))
    ownStock_tmp = 0
    sellStock_tmp = 0
    action_o = 0
    action_u = 0
    tmp = np.zeros(3)

    capital=1
    capitalOrig=capital
    dataCount=len(priceVec)
    suggestedAction=actionVec
    stockHolding=np.zeros((dataCount))
    total = np.zeros((dataCount))
    realAction=np.zeros((dataCount))
    total[0] = capital

    for ic in range(dataCount):
        currPrice = priceVec[ic]
        if ic == 0:
            stockHolding[ic]=capital*(1-transFeeRate)/currPrice
            capital=0
            ownStock[ic][0] = stockHolding[ic]
            ownStock[ic][1] = 1
            ownStock[ic][2] = ownStock[ic][0]*currPrice*(1-transFeeRate)
            unownStock[ic][0] = 1 #captial
            unownStock[ic][1] = 0
        else:
            #calculate own matrix
            stockHolding[ic] = unownStock[ic-1][0]*(1-transFeeRate)/currPrice
#            ownStock_tmp = stockHolding[ic]*currPrice*(1-transFeeRate)
            if stockHolding[ic] > ownStock[ic-1][0]:
                ownStock[ic][0] = stockHolding[ic]
                ownStock[ic][1] = 0
                ownStock[ic][2] = ownStock[ic][0]*currPrice*(1-transFeeRate)
            else:
                ownStock[ic][0] = ownStock[ic-1][0]
                ownStock[ic][1] = 1
                ownStock[ic][2] = ownStock[ic][0]*currPrice*(1-transFeeRate)
                stockHolding[ic] = stockHolding[ic-1]
            #calculate unown matrix
            sellStock_tmp = ownStock[ic-1][0]*currPrice*(1-transFeeRate)
            if sellStock_tmp > unownStock[ic-1][0]:
                unownStock[ic][0] = sellStock_tmp
                unownStock[ic][1] = 1
            else:
                unownStock[ic][0] = unownStock[ic-1][0]
                unownStock[ic][1] = 0
#        if ic == 2:
#            print (ownStock[ic][2], ownStock[ic][1])


#path(ownStock,unownStock,actionVec,dataLen-1)
    for n in range(dataLen-1, -1, -1):
        if n == dataLen-1:
            if ownStock[n][2] > unownStock[n][0]:
                if ownStock[n][1] == 1:
                    tmp = 1
                    actionVec[n] = 0
                elif ownStock[n][1] == 0:
                    tmp = 0
                    actionVec[n] = 1
            else:
                if unownStock[n][1] == 1:
                    tmp = 1
                    actionVec[n] = -1
                elif unownStock[n][1] == 0:
                    tmp = 0
                    actionVec[n] = 0
        elif n == 0:
            if tmp == 1:
                actionVec[n] = 1
            else :
                actionVec[n] = 0
        else:
            if tmp == 1:
                if ownStock[n][1] == 1:
                    tmp = 1
                    actionVec[n] = 0
                elif ownStock[n][1] == 0:
                    tmp =0
                    actionVec[n] = 1
            elif tmp == 0:
                if unownStock[n][1] == 1:
                    tmp = 1
                    actionVec[n] = -1
                elif unownStock[n][1] == 0:
                    tmp = 0
                    actionVec[n] = 0
    return actionVec








