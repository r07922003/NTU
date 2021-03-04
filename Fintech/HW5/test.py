def myOptimAction(priceVec, transFeeRate):
    import numpy as np
    dataLen = len(priceVec)
    actionVec = np.zeros(dataLen)
    dp = np.zeros((dataLen,2))
    temp=1
    temp1=0
    temp2=0
    for i in range(dataLen):
        currPrice = priceVec[i]
        if i == 0: #state 1
            #持有股票的情形
            dp[i][0] = 1*(1-transFeeRate)/currPrice
            #不持有股票的情型
            dp[i][1] = 1
        else:
            #state1:有股票 -> state2:有股票
            #state1:有股票 -> state2:無股票
            dp[i][0] = dp[i-1][0]
            dp[i][1] = dp[i-1][0]*(1-transFeeRate)*currPrice
            #state1:無股票 -> state2:有股票
            #state1:無股票 -> state2:無股票
            temp1 = dp[i-1][1]*(1-transFeeRate)/currPrice
            temp2 = dp[i-1][1]
            if temp1 > dp[i][0]:
                dp[i][0]=temp1
            if temp2 > dp[i][1]:
                dp[i][1]=temp2
    #for i in range(dataLen):
    #    print(dp[i][0],dp[i][1])
    for i in range(dataLen-1,-1,-1):
        if i == dataLen-1:
            if dp[i][0] > dp[i-1][0]:
                actionVec[i] = 1
                temp = 1
            elif dp[i][1] > dp[i-1][1]:
                actionVec[i] = -1
                temp = -1
            else:
                actionVec[i] = 0
        else:
            if temp == -1:
                if dp[i][0]>dp[i-1][0]:
                    actionVec[i] = 1
                    temp = 1
                else:
                    actionVec[i] = 0
            elif temp == 1:
                if dp[i][1]>dp[i-1][1]:
                    actionVec[i] = -1
                    temp = -1
                else:
                    actionVec[i] = 0
        if i==0:
            if temp == -1:
                actionVec[i] = 1
    return actionVec
