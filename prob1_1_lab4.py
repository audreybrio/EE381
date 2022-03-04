import numpy as np
import random
import matplotlib
import math
import matplotlib.pyplot as plt

#simulating uniform random variable
def uniform(a,b):
    #from lab manual
    n = 10000
    x = np.random.uniform(a,b,n)
    #Create bins and histogram
    nbins = 30; # Number of bins
    edgecolor = 'w' # Color separating bars in the bargraph
    bins = [float(x) for x in np.linspace(a, b,nbins+1)]
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
    f = UnifPDF(1,4,b1)
    plt.plot(b1,f,'r')
    #naming
    plt.title("Uniform Random Variable")
    plt.xlabel("Experimental Values")
    plt.ylabel("PDF")
    plt.show()
    #calculate mean and standard deviation
    mu_x = np.mean(x)
    sig_x = np.std(x)
    print("Mean: {:1}".format(mu_x))
    print("Standard Deviation: {:1}".format(sig_x))

#plot uniform pdf from lab manual
def UnifPDF(a,b,x):
    f=(1/abs(b-a))*np.ones(np.size(x))
    return f

#main function
def main():
    a = 1.0
    b = 4.0
    uniform(a,b)

if __name__ == "__main__":
    main()


