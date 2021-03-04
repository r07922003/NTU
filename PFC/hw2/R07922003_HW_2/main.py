import numpy as np

"""
Q:
Write a binomial tree program to calculate the put prices of Bermuda options. 
For such options, early exercise is allowed only on specific dates.

Inputs: 
S (stock price)
X (strike price)
r (continuously compounded annual interest rate in percentage)
s (annual volatility in percentage)
T (time to maturity in days, which of course is also an exercise date)
E (set of early exercise dates from now)
m (number of periods per day for the tree)

Output:
11.2486

Long put:MAX{X-ST,0} 
X (Strike Price)
ST (represent the price of the underlying at maturity)
"""

class node:
    def __init__(self,price):
        self.price = price
        self.value = 0
        self.u_parent = None
        self.d_parent = None
        self.u_child = None
        self.d_child = None

def price(S,X,r,s,T,E,m):
    if T not in E:
        E.append(T)
    deltaT = (T/365)/(T*m)
    R = np.exp(r*deltaT)
    u = np.exp(s*np.sqrt(deltaT))
    d = 1/u
    p = (R - d) / (u-d) #Risk Neutral Probability 
    root = node(S)
    BinomialTree = [[root]]
    
    for period in range(T*m):
        currentLevel = BinomialTree[-1]
        childLevel = [node(currentLevel[0].price * u)]
        #print(childLevel[0].price)
        for currentNode in currentLevel:
            currentNode.u_child = childLevel[-1]
            currentNode.u_child.d_parent = currentNode
            downChild = node(currentNode.price * d)
            downChild.u_parent = currentNode
            currentNode.d_child = downChild
            childLevel.append(downChild)
        BinomialTree.append(childLevel)
        
    total = T * m
    for levelNodes in BinomialTree[::-1]:
        if int(total/m) in E:
            for tree_node in levelNodes:
                if tree_node.u_child != None:
                    binomialValue = ( ( 1/R ) * (p * tree_node.u_child.value + (1 - p) * tree_node.d_child.value))
                else:
                    exerciseValue = max(0,X - tree_node.price)
                    binomialValue = exerciseValue
                    #print(exerciseValue)

                exerciseValue = max(0,X - tree_node.price)
                tree_node.value = max(binomialValue, exerciseValue)
        else:
            for tree_node in levelNodes:
                binomialValue = ( ( 1/R ) * (p * tree_node.u_child.value + (1 - p) * tree_node.d_child.value))
                tree_node.value = binomialValue
        total -= 1

    putPrice = root.value

    return putPrice

if __name__ == "__main__":
    S = float(input("輸入Stock Price ex:100\n"))
    X = float(input("輸入Strike price ex:110\n"))
    r = float(input("輸入Continuously compounded annual interest rate in percentage(%) ex:3\n"))/100
    s = float(input("輸入Annual volatility in percentage(%) ex:30\n"))/100
    T = int(input("輸入time to maturity in days,which of course is also an exercise date ex:60\n"))
    Temp = input("輸入set of early exercise dates from now ex:10 20 30 40 50\n").split(' ')
    E = []
    for temp in Temp:
        E.append(int(temp))
    m = int(input("輸入number of periods per day for the tree ex:5\n"))
    print("S= %f" %S)
    print("X= %f" %X) 
    print("r= %f" %r)
    print("s= %f" %s)
    print("T= %d" %T)
    print("E=",E)
    print("m= %d\n" %m)
    
    output = price(S,X,r,s,T,E,m)
    print(output)