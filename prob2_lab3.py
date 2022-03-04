import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt

#using binomial distribution to get PMF
def bDistribution(p):
    #number of trials 
    n = 1000
    v = 11
    vals = np.zeros((v,1))
    #for different values of X 
    for i in range(0,v):
        #finds success and failure
        success = 0.2*0.1*0.15
        failure = 1 - success
        x = binomial(i,success,failure)
        vals[i] = x
    #plotting
    k = range(0,v+2)
    sz = np.size(k)
    h1, bin_edges = np.histogram(vals, bins=k)
    k1 = bin_edges[0:11]
    plt.close()
    prob = h1/1
    plt.stem(k1, vals)
    #naming
    plt.title('Bernoulli Trials: PMF - Binomial Formula')
    plt.xlabel('Number of successes in n = 1000 trials')
    plt.ylabel('Probability')
    plt.show()

#does one binomial trial
def binomial(r,success,failure):
    #gets comination of n and r
    nfact = factorial(1000)
    nminusr = 1000 - r
    nrfact = factorial(nminusr)
    rfact =factorial(r)
    combo = nfact / ((nrfact)*(rfact))
    #binomial trial formula 
    b = combo * (success ** r) * (failure ** nminusr)
    return b

#gets fctorial of a numeber 
def factorial(n):
    factorial = 1
    if n >= 1:
        for i in range(1,n+1):
            factorial = factorial*i
    return factorial

#main function
def main():
    p=[0.2, 0.1, 0.15, 0.3, 0.2, 0.05]
    bDistribution(p)

if __name__ == "__main__":
    main()