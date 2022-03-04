import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt

def rChooseS(p,e,d):
    success = 0
    sumS = 0
    #gets p1
    q = 1-p
    N = 100000
    #repeats 100000 times
    for i in range(0, N):
        #find s 
        sr = nSidedDie([p,1-p])
        s = sr - 1
        #only care where s = 1
        if s == 1:
            #counts number of times s = 1
            sumS = sumS + 1
            #finding r
            rs1 = nSidedDie([d,1-d])
            r = rs1 - 1
            #if r = 1 and s = 1 it is a success
            if r == 1:
                success = success + 1

    #find the probabilty
    prob = success / sumS
    print("Conditional Probabilty P(R=1|S=1) is p = {:1}".format(prob))


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
    rChooseS(p,e,d)



if __name__ == "__main__":
    main()