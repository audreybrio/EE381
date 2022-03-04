import numpy as np
import random
import matplotlib
import math
import matplotlib.pyplot as plt

#seeing effect of sample size on confidence intervals
def confidence(N,mean,sd,sample):
    #instatiate lists
    p_95 = [] 
    m_95 = []
    p_99 = []
    m_99 = []
    x_plot = []
    mu = []
    #do it for all n = 1...200
    for i in range(1,sample+1):
        #95% inteval
        p = nine_five(mean,sd,i)
        q = n_f(mean,sd,i)
        p_95.append(p)
        m_95.append(q)  
        #99% interval
        x = nine_nine(mean,sd,i)
        y = n_n(mean,sd,i)
        p_99.append(x)
        m_99.append(y) 
        #line for mean
        mu.append(mean)   
        #x marks for sample means
        f = random_sample(mean,sd,i) 
        x_plot.append(f)

    #plot 95% confidence interval
    fig1 = plt.figure(1)
    #upper and lower lines
    plt.plot(range(sample),p_95, linestyle = 'dashed', linewidth = 1, color = 'Red')
    plt.plot(range(sample),m_95, linestyle = 'dashed', linewidth = 1, color = 'Red')
    #mean line
    plt.plot(range(sample),mu,linestyle = 'solid', linewidth = 1, color = 'Black')
    #x marks
    plt.plot(range(sample),x_plot,'bx')
    #naming
    plt.title("Sample Means and 95% Confidence Intervals")
    plt.xlabel("Sameple Size")
    plt.ylabel("X_bar")
    plt.show

    #plot 99% confidence interval
    fig2 = plt.figure(2)
    #upper and lower lines
    plt.plot(range(sample),p_99, linestyle = 'dashed', linewidth = 1, color = 'Green')
    plt.plot(range(sample),m_99, linestyle = 'dashed', linewidth = 1, color = 'Green')
    #mean line
    plt.plot(range(sample),mu,linestyle = 'solid', linewidth = 1, color = 'Black')
    #x marks
    plt.plot(range(sample),x_plot,'bx')
    #naming
    plt.title("Sample Means and 99% Confidence Intervals")
    plt.xlabel("Sameple Size")
    plt.ylabel("X_bar")
    plt.show()

#gets random sample of size n and fins the mean
def random_sample(mu, sig, n):
    x = np.random.normal(mu,sig,n)
    sums = np.sum(x)
    mean = sums / n
    return mean

#gets addition part of 95 condifence interval
def nine_five(mean, sd, n):
    plus = mean + (1.96)*(sd/np.sqrt(n))
    return plus

#gets subtraction part of 95 condifence interval
def n_f(mean,sd,n):
    minus =  mean - (1.96)*(sd/np.sqrt(n))
    return minus

#gets addition part of 99 condifence interval
def nine_nine(mean, sd, n):
    plus = mean + (2.58)*(sd/np.sqrt(n))
    return plus

#gets subtraction part of 99 condifence interval
def n_n(mean,sd,n):
    minus =  mean - (2.58)*(sd/np.sqrt(n))
    return minus

#main function
def main():
    N = 1500000
    mean = 55
    sd = 5
    sample = 200
    confidence(N,mean,sd,sample)
    

if __name__ == "__main__":
    main()