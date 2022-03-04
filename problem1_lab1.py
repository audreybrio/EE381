import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt

#uses probs to roll random n sided die 
def nSidedDie(p):
    N = 10000
    rand=0
    cs = np.cumsum(p)
    cp = np.append(0,cs)
    n = np.size(p)
    rand = random.random()
    dj = 0
    #random number that is rolled
    for k in range(0,n):
        if rand > cp[k] and rand <= cp[k+1]:
            dj = k+1
            break
    return dj


#rolls random number and plots PMF
def roll(p):
    N = 10000
    n = np.size(p)
    s = np.zeros((N,1))
    #runs expeiment 10000 times
    for i in range(0,N):
        r = nSidedDie(p)
        s[i] = r
    #plotting
    d = range(1,n+2)
    sz = np.size(d)
    h1, bin_edges = np.histogram(s, bins=d)
    d1 = bin_edges[0:7]
    plt.close()
    prob = h1/N
    plt.stem(d1, prob)
    #naming
    plt.title('Stem Plot - Single Roll for an N-Sided Die')
    plt.xlabel('Number on face of die')
    plt.ylabel('Probability') #i dont think its prob
    plt.show()

#checks to see if probabilities add up to one
def check(p):
    my = 0
    for i in p:
        my = my + i
    if  my == 1:
        return True
    else:
        return False  

#main function
def main():
    p = np.array([0.10,0.15,0.20,0.05,0.30,0.10,0.10])
    d = check(p)
    if d == True:
        roll(p)
    else:
        print("The probabilty values are incorect. Please fix.")



if __name__ == "__main__":
    main()