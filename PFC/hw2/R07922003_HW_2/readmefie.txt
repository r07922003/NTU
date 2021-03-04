執行 python main.py
依序輸入

Inputs: 
S (stock price)
X (strike price)
r (continuously compounded annual interest rate in percentage)
s (annual volatility in percentage)
T (time to maturity in days, which of course is also an exercise date)
E (set of early exercise dates from now)
m (number of periods per day for the tree)

S = 100
X = 110
r = 3 #3%
s = 30 #30%
T = 60
E = 10 20 30 40 50
m = 5

Output:
11.2486 (example)