import numpy as np
import random
import matplotlib
import math
import matplotlib.pyplot as plt

#uses poisson to approximate prob of success in n trials
def poisson():
    n = 1000
    v = 11
    vals = np.zeros((v,1))
    #for different values of X
    for i in range(0,v):
        #finds success and failure
        success = 0.2*0.1*0.15
        x = pois(i,n,success)
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
    plt.title('Bernoulli Trials: PMF - Poisson Approximation')
    plt.xlabel('Number of successes in n = 1000 trials')
    plt.ylabel('Probability')
    plt.show()

#finds poisson based on how to in lab manual
def pois(x,n,p):
    #getting lambda
    lamb = n*p
    xfact = factorial(x)
    #numerator of formaula
    temp = (lamb ** x) * (math.e ** (-lamb))
    #doing the formula
    po = temp / xfact
    return po

#finds the factorial of a number 
def factorial(n):
    factorial = 1
    if n >= 1:
        for i in range(1,n+1):
            factorial = factorial*i
    return factorial

#main function
def main():
    p=[0.2, 0.1, 0.15, 0.3, 0.2, 0.05]
    poisson()

if __name__ == "__main__":
    main()