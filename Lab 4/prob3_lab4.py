import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt

#distribution of the sum of the exponential random variables
def distribution(beta):
    n = 10000
    total = np.zeros((n,1))
    c=0
    #doing it 10000 times
    for i in range(0,n):
        #getting random var
        x = np.random.exponential(beta,24)
        #getting sum of random variables
        c = np.sum(x)
        total[i] = c
    mu_x = 24*beta
    sig_x = np.sqrt(24)*beta
    nbins = 30; # Number of bins
    edgecolor = 'w' # Color separating bars in the bargraph
    bins = [float(x) for x in np.linspace(mu_x - 3*sig_x,mu_x + 3*sig_x,nbins+1)]
    h1, bin_edges = np.histogram(total,bins,density=True)
    # Define points on the horizontal axis
    be1 = bin_edges[0:np.size(bin_edges)-1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 = (be1+be2)/2
    barwidth = b1[1]-b1[0] # Width of bars in the bargraph
    plt.close('all')
    # PLOT THE BAR GRAPH
    fig1 = plt.figure(1)
    plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)
    #normal rv pdf
    g = NormfPDF(mu_x, sig_x, b1)
    plt.plot(b1,g, 'r') #normal: red line
    #naming 
    plt.title("Distribution of the Sum of Experimental Random Variables")
    plt.xlabel("Sum of 24 cartons")
    plt.ylabel("PDF")
    plt.show()
    #finding cdf
    cdf = np.cumsum(h1) * barwidth
    #plotting cdf   
    plt.plot(bin_edges[1:], cdf, label = "CDF")
    #naming
    plt.title("Lifetime of a Carton")
    plt.xlabel("Days")
    plt.ylabel("CDF")
    plt.show()

#normal rv pdf from lab manual
def NormfPDF(mu,sigma,x):
    f = np.exp(-(x-mu)**2/(2*sigma**2))/(sigma*np.sqrt(2*np.pi))
    return f

#main function
def main():
    beta = 40
    distribution(beta)

if __name__ == "__main__":
    main()