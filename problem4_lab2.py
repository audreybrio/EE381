import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt

def enhanced(p,e,d):
    success = 0
    N = 100000
    q = 1-p
    for i in range(0, N):
        # finding s 
        sr = nSidedDie([p,q])
        s = sr - 1
        #finding r values
        if s == 1:
            # does it 3 times
            ar = nSidedDie([d,1-d])
            a = ar - 1
            br = nSidedDie([d,1-d])
            b = br - 1
            cr = nSidedDie([d,1-d])
            c = cr - 1
        elif s == 0:
            #does it 3 times 
            ar = nSidedDie([1-e,e])
            a = ar - 1
            br = nSidedDie([1-e,e])
            b = br - 1
            cr = nSidedDie([1-e,e])
            c = cr - 1
        #adding them together 
        majority = a+b+c
        #using the voting rule
        if majority == 1 or majority == 0:
            dd = 0
        elif majority == 2 or majority == 3:
            dd = 1
        #finding number of successes
        if dd == s:
            success = success + 1
    #finding prob of failure
    temp = success / N
    prob = 1 - temp

    print("Probability of error with enhanced transmission is p = {:1}".format(prob))

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
    enhanced(p,e,d)

if __name__ == "__main__":
    main()