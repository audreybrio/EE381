import numpy as np
import random
import math
import matplotlib
import matplotlib.pyplot as plt

#simulate normal random vaiable
def normal(mu, sigma):
    #from lab manual
    n = 10000
    x = np.random.normal(mu, sigma, n)
    # Create bins and histogram
    nbins = 30; # Number of bins
    edgecolor = 'w' # Color separating bars in the bargraph
    bins = [float(x) for x in np.linspace(mu-3*sigma,mu+3*sigma,nbins+1)]
    h1, bin_edges = np.histogram(x,bins,density=True)
    # Define points on the horizontal axis
    be1 = bin_edges[0:np.size(bin_edges)-1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 = (be1+be2)/2
    barwidth = b1[1]-b1[0] # Width of bars in the bargraph
    plt.close('all')
    #plot graph
    fig1 = plt.figure(1)
    plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)
    f = NormfPDF(mu,sigma,b1)
    plt.plot(b1,f,'r')
    #naming
    plt.title("Normal Random Variable")
    plt.xlabel("Experimental Values")
    plt.ylabel("PDF")
    plt.show()
    #calculate mean and standard deviation
    mu_x = np.mean(x)
    sig_x = np.std(x)
    print("Mean: {:1}".format(mu_x))
    print("Standard Deviation: {:1}".format(sig_x))

#plit normal pdf from lab manual
def NormfPDF(mu,sigma,x):
    f = np.exp(-(x-mu)**2 / (2*sigma ** 2))/ (sigma*np.sqrt(2*np.pi))
    return f

#main function
def main():
    mu = 2.5
    sigma = 0.75
    normal(mu,sigma)

if __name__ == "__main__":
    main()