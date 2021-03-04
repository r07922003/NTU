##### x-year American-style put option on a zero coupon bond that matures at year y with a par value of 1 dollar.
#Use binomial trees for the CIR model
import numpy as np
import sys
'''
Inputs: 
x (year)
y (year)
r (%) (initial short rate)
b (%)
m (%)
s (%)
n number of partitions during the option's life
X strike price (% of par).


x = 1
y = 3
r = 1 #%
b = 30 #(%)
m = 2 #(%)
s = 30 #(%)
n = 150
X = 95 #(%)

#output 1.01555 (%)

#output4.42332 (% of par) 
x = 1
y = 2
r = 5
b = 10 
m = 6 
s = 30
n = 100 
X = 95
'''
x = float(sys.argv[1])
y = float(sys.argv[2])
r = float(sys.argv[3])
b = float(sys.argv[4])
m = float(sys.argv[5])
s = float(sys.argv[6])
n = int(sys.argv[7])
X = float(sys.argv[8])


class node:
    def __init__(self,x,s):
        self.x = x
        self.r = (x**2)*((s/100)**2)/4
        self.price = 0
        self.value = 0
        self.prob = 0
        self.u_parent = None
        self.d_parent = None
        self.u_child = None
        self.d_child = None

deltaT = x/n

#generate short rate tree
root = node(2*np.sqrt(r/100)/(s/100),s)
levels = [[root]]
for i in range(n):
    currentLevel = levels[-1]
    childLevel = [node(x=currentLevel[0].x + np.sqrt(deltaT),s=s)]
    for currentNode in currentLevel:
        currentNode.u_child = childLevel[-1]
        currentNode.u_child.d_parent = currentNode
        downChild = node(x=currentNode.x - np.sqrt(deltaT),s=s)
        downChild.u_parent = currentNode
        currentNode.d_child = downChild
        childLevel.append(downChild)
    levels.append(childLevel)

#generate prob

for i in range(len(levels)-1):
    for tree_node in levels[i]:
        now_r = tree_node.r
        up_r = tree_node.u_child.r
        down_r = tree_node.d_child.r
        tree_node.prob = ((b/100)*(m/100-now_r)*deltaT+now_r-down_r) / (up_r-down_r)
        if tree_node.prob > 1:
            tree_node.prob = 1
        if tree_node.prob < 0:
            tree_node.prob = 0
#generate price

price_a = (b/100)*(m/100)
price_b = b/100
c1 = np.sqrt(price_b**2+2*((s/100)**2))
c2 = (price_b+c1)/2
c3 = 2*price_a/((s/100)**2)

for i in range(len(levels)):
    price_s = y-i*deltaT
    A_t = (c1*np.exp(c2*price_s) / (c2*(np.exp(c1*price_s)-1)+c1))**c3
    C_t = (np.exp(c1*price_s)-1) / (c2*(np.exp(c1*price_s)-1)+c1)
    for tree_node in levels[i]:
        now_r = tree_node.r
        tree_node.price = A_t*np.exp(-1*C_t*now_r)
        
# go back calculate value
Strike = X/100
#計算最後一層value
for tree_node in levels[-1]:
    tree_node.value = max(Strike-tree_node.price,0)
for i in range(len(levels)-2,-1,-1):
    for tree_node in levels[i]:
        q = tree_node.prob
        discount_factor = 1/np.exp(tree_node.r*deltaT)
        tree_node.value = max(Strike-tree_node.price,
            (q*tree_node.u_child.value + (1-q)*tree_node.d_child.value)*discount_factor
                             )
        
"""
#debug show x
for i in levels:
    print(len(i),":")
    for line in i:
        print("  ",line.value)
"""
print("the option price is about %.5f (%% of par)" %(levels[0][0].value*100))