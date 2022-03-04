import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt

#central limit theorem
def clt(a,b,nbooks):
    # Generate the values of the RV X
    N = 10000
    mu_x = (a+b)/2
    sig_x = np.sqrt((b-a)**2/12)
    X = np.zeros((N,1))
    for k in range(0,N):
        x = np.random.uniform(a,b,nbooks)
        w = np.sum(x)
        X[k] = w
    # Create bins and histogram
    nbins = 30; # Number of bins
    edgecolor = 'w'; # Color separating bars in the bargraph
    bins = [float(x) for x in np.linspace(nbooks*a, nbooks*b,nbins+1)]
    h1, bin_edges = np.histogram(X,bins,density=True)
    # Define points on the horizontal axis
    be1 = bin_edges[0:np.size(bin_edges)-1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 = (be1+be2)/2
    barwidth = b1[1]-b1[0] # Width of bars in the bargraph
    plt.close('all')
    #plot grapgh
    fig1 = plt.figure(1)
    plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)
    f = gaussian(mu_x*nbooks,sig_x*np.sqrt(nbooks),b1)
    plt.plot(b1,f,'r')
    #naming
    plt.title("PDF of book stack height and comparison with Gaussian")
    plt.xlabel("Book stack height for n = {:1} books".format(nbooks))
    plt.ylabel("PDF")
    plt.show()

#PLOT THE GAUSSIAN FUNCTION
def gaussian(mu,sig,z):
    f = np.exp(-(z-mu)**2/(2*sig**2))/(sig*np.sqrt(2*np.pi))
    return f

#main function
def main():
    a = 1.0
    b = 4.0
    one = 1
    five = 5
    fif = 15
    clt(a,b,one)
    clt(a,b,five)
    clt(a,b,fif)

if __name__ == "__main__":
    main()