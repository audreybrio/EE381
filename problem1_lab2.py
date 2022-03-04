import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt

#p = p0
#q = p1
#e = e0
#d = e1

#finds probabilty of failure
def eTrans(p, e, d):
    failure = 0
    #gets p1
    q = 1-p
    N = 100000
    #repeats 100000 times
    for i in range(0, N):
        #finds value of S based from lab document 
        sr = nSidedDie([p,q])
        s = sr - 1
        # find value of r
        if s == 1:
            rs1 = nSidedDie([d,1-d])
            r = rs1 - 1
        elif s == 0:
            rs2 = nSidedDie([1-e,e])
            r = rs2 - 1
        #counts number of times it fails
        if s != r:
            failure = failure + 1
    #finds probabilty
    prob = failure / N
    print("Probabilty of transmission error is p = {:1}".format(prob))

#n sided die function from last lab to get s and r
def nSidedDie(p):
    n=np.size(p)
    cs=np.cumsum(p)
    cp=np.append(0,cs)
    r=random.random()
    for k in range(0,n):
        if r>cp[k] and r<=cp[k+1]:
            d=k+1
            break
    return d

#main function 
def main():
    p = 0.6
    e = 0.05
    d = 0.03
    eTrans(p,e,d)

if __name__ == "__main__":
    main()