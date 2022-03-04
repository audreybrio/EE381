import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt

#keeps track of number of times until rolls a seven
def rollASeven():
    count = 0
    while True:
        count = count + 1
        a = random.randint(1,6)
        b = random.randint(1,6)
        if a+b == 7:
            return count
            #breaks when roll is a seven
            break


#runs experiment 100000 times
def sumOfDie():
    N = 10000
    d = np.zeros((N,1))
    for i in range(0,N):
        r = rollASeven()
        #keeps a list of how long inbwetween successes
        d[i] = r
    
    #plotting
    k = range(1,22)
    sz = np.size(k)
    h1, bin_edges = np.histogram(d, bins=k)
    k1 = bin_edges[0:20]
    plt.close()
    prob = h1/N
    plt.stem(k1, prob)
    #naming
    plt.title('Bernoulli Trials: PMF - Experimental Results')
    plt.xlabel('Number of successes in n = 1000 trials ')
    plt.ylabel('Probability')
    plt.show()

#main function
def main():
    sumOfDie()

if __name__ == "__main__":
    main()