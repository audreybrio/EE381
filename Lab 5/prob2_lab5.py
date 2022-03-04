import numpy as np
import random
import matplotlib
import math
import matplotlib.pyplot as plt

#using sample mean to estimate population mean
def population(N,mean,sd,sample):
    nn = 10000
    success_N = 0 #95 normal success
    success_t = 0 #95 t dist success
    s_N = 0 #99 normal success
    s_t = 0 #99 t dist success
    #sample of N size
    z = np.random.normal(mean,sd,N)
    #doing it 10000 times 
    for i in range(0, nn):    
        x = []
        #gets n = 5 / 40 / 120 sample out of N
        for j in range(0,sample):
            x.append(random.choice(z))
        #finds mean and sd of sample size 
        mu = sample_mean(x,sample)
        sigma = sample_sd(x,mu,sample)
        #normal distriution for 95
        upper_95, lower_95 = normal_95(mu,sigma,sample)
        if(lower_95 <= mean <= upper_95):
            success_N = success_N + 1
        #t dist for 95
        u_95, l_95 = t_dist_95(mu,sigma,sample)
        if(l_95 <= mean <= u_95):
            success_t = success_t + 1
        #normal distribution for 99
        upper_99, lower_99 = normal_99(mu,sigma,sample)
        if(lower_99 <= mean <= upper_99):
            s_N = s_N + 1
        #t dist for 99
        u_99, l_99 = t_dist_99(mu,sigma,sample)
        if(l_99 <= mean <= u_99):
            s_t = s_t + 1

    print("Pecentage of normal success for 95 percent interval for n = {:1} sample size is {:1}%".format(sample,success_N/100))
    print("Pecentage of t-dist success for 95 percent interval for n = {:1} sample size is {:1}%".format(sample,success_t/100))
    print("Pecentage of normal success for 99 percent interval for n = {:1} sample size is {:1}%".format(sample,s_N/100))
    print("Pecentage of t-dist success for 99 percent interval for n = {:1} sample size is {:1}%\n".format(sample,s_t/100))

#gets sample mean from lab manual
def sample_mean(x,n):
    sums = np.sum(x)
    mean = sums / n
    return mean

#gets sample sd from lab manual
def sample_sd(x, s_mean, n):
    temp = []
    for i in x:
        f = ((i - s_mean) ** 2)
        temp.append(f)
    sums = np.sum(temp)
    sd = sums / (n-1)
    h = np.sqrt(sd)
    return h

#normal dist for 95 confidence interval
def normal_95(mean,sd,n):
    plus = mean + (1.96)*(sd/np.sqrt(n)) 
    minus = mean - (1.96)*(sd/np.sqrt(n))
    return plus,minus

#normal dist for 99 confidence interval
def normal_99(mean,sd,n):
    plus = mean + (2.58)*(sd/np.sqrt(n)) 
    minus = mean - (2.58)*(sd/np.sqrt(n))
    return plus,minus

#t dist for 95 confidence interval
def t_dist_95(mean,sd,n):
    if n == 5:
        plus = mean + (2.78)*(sd/np.sqrt(n)) 
        minus = mean - (2.78)*(sd/np.sqrt(n))
    elif n == 40:
        plus = mean + (2.023)*(sd/np.sqrt(n)) 
        minus = mean - (2.023)*(sd/np.sqrt(n))
    elif n == 120:
        plus = mean + (1.96)*(sd/np.sqrt(n)) 
        minus = mean - (1.96)*(sd/np.sqrt(n))
    return plus,minus

#t dist for 99 confidence interval
def t_dist_99(mean,sd,n):
    if n == 5:
        plus = mean + (4.60)*(sd/np.sqrt(n)) 
        minus = mean - (4.60)*(sd/np.sqrt(n))
    elif n == 40:
        plus = mean + (2.708)*(sd/np.sqrt(n)) 
        minus = mean - (2.708)*(sd/np.sqrt(n))
    elif n == 120:
        plus = mean + (2.576)*(sd/np.sqrt(n)) 
        minus = mean - (2.576)*(sd/np.sqrt(n))
    return plus,minus

#main function
def main():
    N = 1500000
    mean = 55
    sd = 5
    population(N,mean,sd,5)
    population(N,mean,sd,40)
    population(N,mean,sd,120)

if __name__ == "__main__":
    main()