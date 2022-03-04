import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt

#absorbing to 0
def five():
    n = 15
    state = []
    s = []
    #equal chance of startng at state 1,2,or 3
    a = nSidedDie([1/3,1/3,1/3])
    state.append(a)
    for i in range(1,n):
        #finding next state if state is at 1
        if a == 1:
            b = nSidedDie([0.3,0.7])
            #change numbers 
            if b == 1:
                a = 0
                state.append(a)
            else:
                a = 2
                state.append(a)
        #finding next state if state is at 2
        elif a == 2:
            b = nSidedDie([0.5,0.5])
            #change number 
            if b == 1:
                a = 1
                state.append(a)
            else:
                a = 3
                state.append(a)
        #finding next state if state is at 3
        elif a == 3:
            b = nSidedDie([0.6,0.4])
            #change numbers 
            if b == 1:
                a = 2
                state.append(a)
            else:
                a = 4
                state.append(a)
        #finding next state if state is at 0
        elif a == 0:
            a = 0
            state.append(a)
        #finding next state if state is at 4
        elif a == 4:
            a = 4
            state.append(a)
    #seeing what the last state is and if its 0 plot it
    if state[-1] == 0:
        plot(n,state)
    #if not run it again 
    else:
        five()

#absorbing to 4
def six():
    n = 15
    state = []
    s = []
    #equal chance of startng at state 1,2,or 3
    a = nSidedDie([1/3,1/3,1/3])
    state.append(a)
    for i in range(1,n):
        #finding next state if state is at 1
        if a == 1:
            b = nSidedDie([0.3,0.7])
            #change numbers
            if b == 1:
                a = 0
                state.append(a)
            else:
                a = 2
                state.append(a)
        #finding next state if state is at 2
        elif a == 2:
            b = nSidedDie([0.5,0.5])
            #change numbers
            if b == 1:
                a = 1
                state.append(a)
            else:
                a = 3
                state.append(a)
        #finding next state if state is at 3
        elif a == 3:
            b = nSidedDie([0.6,0.4])
            #change numbers
            if b == 1:
                a = 2
                state.append(a)
            else:
                a = 4
                state.append(a)
        #finding next state if state is at 0
        elif a == 0:
            a = 0
            state.append(a)
        #finding next state if state is at 4
        elif a == 4:
            a = 4
            state.append(a)
    #seeing what the last state is and if its 4 plot it
    if state[-1] == 4:
        plot(n,state)
    #if not run it again 
    else:
        six()

#plotting 
def plot(n, state):
    fig1 = plt.figure(1)
    #lines
    #so see all 4 places
    worry = [0,0,0,1,1,1,2,2,2,3,3,3,4,4,4]
    plt.plot(range(n), worry, color = 'White')
    #actual lines 
    plt.plot(range(n),state, linestyle = 'dashed', linewidth = 1, color = 'Blue')
    plt.plot(range(n),state,'ro')
    #naming
    plt.title("Sample of Drunkard's Walk")
    plt.xlabel("Step Number")
    plt.ylabel("State")
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
    five()
    six()

if __name__ == "__main__":
    main()