import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt

def sChooseR(p,e,d):
    success = 0
    sumR = 0
    #gets p1
    q = 1-p
    N = 100000
    #repeats 100000 times
    for i in range(0, N):
        #finding s
        sr = nSidedDie([p,q])
        s = sr - 1
        # finding r
        if s == 1:
            rs1 = nSidedDie([d,1-d])
            r = rs1 - 1
        # finding r
        elif s == 0:
            rs2 = nSidedDie([1-e,e])
            r = rs2 - 1
        # if r = 1 looking at if s = 1
        if r == 1:
            #counting number of times r = 1
            sumR = sumR + 1
            if s == 1:
                #if both 1, it is a success
                success = success + 1

    #find the probabilty
    prob = success / sumR
    print("Conditional Probabilty P(S=1|R=1) is p = {:1}".format(prob))


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
    sChooseR(p,e,d)
    

if __name__ == "__main__":
    main()