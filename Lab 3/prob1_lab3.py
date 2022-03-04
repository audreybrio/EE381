import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt

#rolls 3 dice and finds nummber of successes in n = 1000
def bTrials(p):
    N = 1000
    success = 0
    for i in range(0,N):
        roll1 = nSidedDie(p)
        roll2 = nSidedDie(p)
        roll3 = nSidedDie(p)
        #if it is a success, keep track of how many
        if roll1 == 1 and roll2 == 2 and roll3 == 3:
            success = success + 1
    x = success
    #return the number of successes
    return x

#repeat n = 10000 times and get PMF
def experiment(p):
    N = 10000
    vals = np.zeros((N,1))
    #does above bTrails 10,000 time and keeps track of x = number of successes in 1000 trials for each one
    for i in range(0, N):
        x = bTrials(p)
        vals[i] = x
    #plotting
    k = range(0,12)
    sz = np.size(k)
    h1, bin_edges = np.histogram(vals, bins=k)
    k1 = bin_edges[0:11]
    plt.close()
    prob = h1/N
    plt.stem(k1, prob)
    #naming
    plt.title('Bernoulli Trials: PMF - Experimental Results')
    plt.xlabel('Number of successes in n = 1000 trials')
    plt.ylabel('Probability')
    plt.show()

#rolling a die, using this from first lab assignment 
def nSidedDie(p):
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

#main function
def main():
    p = [0.2, 0.1, 0.15, 0.3, 0.2, 0.05]
    experiment(p)

if __name__ == "__main__":
    main()