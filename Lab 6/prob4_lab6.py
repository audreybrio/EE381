import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt

#running single simulation of chain 10000 times
def five(n):
    N = 10000
    tfour = 0
    tzero = 0
    #loop 10000 times 
    for i in range(0,N):
        #get a single run of chain
        x = temp(n)
        #see last value of chain and keep track how many times 0 and how many times 4
        if x[-1] == 0:
            tzero = tzero + 1
        elif x[-1] == 4:
            tfour = tfour + 1
    #probailities 
    prob_1 = tzero / N
    prob_2 = tfour / N
    prob_3 = (tfour + tzero) / N
    print("Probability of n = {:1} ending in 0 is {:1}".format(n,prob_1))
    print("Probability of n = {:1} ending in 4 is {:1}".format(n,prob_2))
    print("Total probability of n = {:1} ending in absorption is {:1}".format(n,prob_3))

#single run of chain from prob 3
def temp(n):
    state = []
    s = []
    #always starting at state 2 
    a = 2
    state.append(a)
    for i in range(1,n):
        #finding next state if at state 1
        if a == 1:
            b = nSidedDie([0.3,0.7])
            if b == 1:
                a = 0
                state.append(a)
            else:
                a = 2
                state.append(a)
        #finding next state if at state 2
        elif a == 2:
            b = nSidedDie([0.5,0.5])
            if b == 1:
                a = 1
                state.append(a)
            else:
                a = 3
                state.append(a)
        #finding next state if at state 3
        elif a == 3:
            b = nSidedDie([0.6,0.4])
            if b == 1:
                a = 2
                state.append(a)
            else:
                a = 4
                state.append(a)
        #finding next state if at state 0
        elif a == 0:
            a = 0
            state.append(a)
        #finding next state if at state 4
        elif a == 4:
            a = 4
            state.append(a)
    #return list of states
    return state

#n sided die function from first lab 
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
    n1 = 20
    n2 = 24
    five(n1)
    five(n2)

if __name__ == "__main__":
    main()