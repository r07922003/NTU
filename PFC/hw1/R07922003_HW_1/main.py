#INPUT (1) s (spot rates) (2) C (cash flows)
#OUTPUT (1) modified duration (2) convexity

# modified duration 4.5624 convexity 0.2588

def getPV(s,C,omega,n):
    pv = 0
    for i in range(n):
        pv += C[i]/ ((1+s[i])**(omega+i))
        #print("pv =",pv)
    return pv

def getYield(pv,s,C,omega,n):
    Yield = 0.001
    for t in range(10000):
        #The Newton-Raphson Method
        F_of_y = 0
        F_pron_of_y = 0
        for i in range(n):
            F_of_y += C[i]/((1+Yield)**(i+1))
            F_pron_of_y += -1 * ((i+1)*C[i])/((1+Yield)**(i+2))
        F_of_y -= pv
        Yield = Yield - F_of_y/F_pron_of_y
    #print("Yield =",Yield)
    return Yield

def get_MD(pv,s,C,omega,n,Yield):
    MD = 0
    for i in range(n):
        MD += (i+omega)*C[i] / ((1+s[i])**(i+omega))
    MD = round((MD/pv) / (1+Yield),4)
    print("modified duration =",MD)
    return MD

def get_Convexity(pv,s,C,omega,n,Yield):
    Convexity = 0
    for i in range(n):
        Convexity += C[i]*(omega+i+1)*(omega+i) / ((1+s[i])**(omega+i+2))
    Convexity /= 100*pv
    Convexity = round(Convexity,4)
    print("Convexity =",Convexity)
    return Convexity

if __name__ == "__main__":
    Temp = input("輸入spot rates,ex:0.053,0.051,0.049,0.047,0.040\n").split(",")
    s = []
    for temp in Temp:
        try:
            s.append(float(temp))
        except:
            pass
    Temp = input("輸入cash flows,ex:3,2,3,2,103\n").split(",")
    C = []
    for temp in Temp:
        try:
            C.append(float(temp))
        except:
            pass
    omega = 1
    n = len(s)

    pv = getPV(s,C,omega,n)
    Yield = getYield(pv,s,C,omega,n)
    modified_duration = get_MD(pv,s,C,omega,n,Yield)
    Convexity = get_Convexity(pv,s,C,omega,n,Yield)
    
    