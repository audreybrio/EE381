import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt
from numpy.linalg import matrix_power

#first part, finding one run of 15 steps
def three(n):
    x = []
    #random choice of where going first
    w = [1/3,1/3,1/3]
    h = nSidedDie(w)
    x.append(h)
    #for rest of states
    for i in range(1,n):
        #finding next state if at state 1
        if h == 1:
            h = nSidedDie([0.5,0.25,0.25])
            x.append(h)
        #finding next state if at state 2
        elif h == 2:
            h = nSidedDie([1/4,1/8,5/8])
            x.append(h)
        #finding next stat if at state 3
        elif h == 3:
            h = nSidedDie([1/3,2/3,0])
            x.append(h)
    #plotting
    fig1 = plt.figure(1)
    #lines
    plt.plot(range(n),x, linestyle = 'dashed', linewidth = 1, color = 'Blue')
    plt.plot(range(n),x,'ro')
    #naming
    plt.title("Sample Simulation Run of a three-state Markov Chain ")
    plt.xlabel("Step Number")
    plt.ylabel("State")
    plt.show()

#same thing from first part minus the plotting 
def temp(n):
    x = []
    #starting values
    w = [0.38,0.55,0.07]
    h = nSidedDie(w)
    x.append(h)
    #for rest of states
    for i in range(1,n):
        #finding next state if at state 1
        if h == 1:
            h = nSidedDie([0.5,0.25,0.25])
            x.append(h)
        #finding next state if at state 2
        elif h == 2:
            h = nSidedDie([1/4,1/8,5/8])
            x.append(h)
        #finding next state if at state 3
        elif h == 3:
            h = nSidedDie([1/3,2/3,0])
            x.append(h)
    return x

#for second part, to do N = 10000 runs of chain 
def two(q):
    n = 14
    N = 10000
    #putting initial values q into list
    one = []
    one.append(q.item(0))
    to = []
    to.append(q.item(1))
    three = []
    three.append(q.item(2))
    mat = []
    #getting list of 10000 runs of the 15 step
    for i in range(0, N):
        x = temp(n)
        mat.append(x)
    #going through 14 states 
    for j in range(0,14):
        o = 0
        t = 0
        th = 0
        #counting how many times is at each state in jth place of 15 steps 
        #ie how many times 1 happened in the 1st step, 2 happened in the first step, etc
        for i in mat:
            if i[j] == 1:
                o = o +1
            elif i[j] == 2:
                t = t+1
            elif i[j] == 3:
                th = th +1
        #finding probability
        prob_1 = o / N
        prob_2 = t / N
        prob_3 = th / N
        #adding them to list to plot
        one.append(prob_1)
        to.append(prob_2)
        three.append(prob_3)
    #plotting
    fig1 = plt.figure(1)
    #lines for state 1, 2 and 3
    plt.plot(range(15),one, linestyle = 'dashed', linewidth = 1, color = 'Blue', label = 'State 1')
    plt.plot(range(15),one,'bo')
    plt.plot(range(15),to, linestyle = 'dashed', linewidth = 1, color = 'Red',  label = 'State 2')
    plt.plot(range(15),to,'ro')
    plt.plot(range(15),three, linestyle = 'dashed', linewidth = 1, color = 'Green',  label = 'State 3')
    plt.plot(range(15),three,'go')
    legend = plt.legend(loc = 'upper right', shadow = True)
    #naming
    plt.title("Simulated three-state Markov Chain ")
    plt.xlabel("Step Number")
    plt.ylabel("Probability")
    plt.show()

#for third part, using state transition matrix approach 
def one(p,q):
    n = 14
    #puting initial values q into lists
    on = []
    on.append(q.item(0))
    two = []
    two.append(q.item(1))
    three = []
    three.append(q.item(2))
    #creating temp value that is equal to q
    temp = q
    for i in range(1,n+1):
        #matrix multiplication
        a = temp * p
        #setting new value to temp so can use on next iteration
        temp = a
        #getting values at each place
        o = a.item(0)
        t = a.item(1)
        th = a.item(2)
        #adding to list to plot
        on.append(o)
        two.append(t)
        three.append(th)
    #plotting
    fig1 = plt.figure(1)
    #lines for state 1,2 and 3
    plt.plot(range(15),on, linestyle = 'dashed', linewidth = 1, color = 'Blue',  label = 'State 1')
    plt.plot(range(15),on,'bo')
    plt.plot(range(15),two, linestyle = 'dashed', linewidth = 1, color = 'Red',  label = 'State 2')
    plt.plot(range(15),two,'ro')
    plt.plot(range(15),three, linestyle = 'dashed', linewidth = 1, color = 'Green',  label = 'State 3')
    plt.plot(range(15),three,'go')
    legend = plt.legend(loc = 'upper right', shadow = True)
    
    #naming
    plt.title("Calculated three-state Markov Chain ")
    plt.xlabel("Step Number")
    plt.ylabel("Probability")
    plt.show()

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
    p = [[1/2,1/4,1/4],[1/4,1/8,5/8],[1/3,2/3,0]]
    q = np.matrix([[0.25,0,0.75]])
    three(15)
    two(q) 
    one(p,q)

if __name__ == "__main__":
    main()

