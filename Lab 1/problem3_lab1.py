import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt

#runs experiment 100000 times
def coinFlip():
    prob = 0
    for j in range(0,100000):
        count = 0
        #flipping coin 100 times
        for i in range(0,100):
            a = random.randint(1,2)
            if a == 1:
                #keeps track of number of heads in 100 rolls
                count = count + 1
        #if total number of heads is 50        
        if count == 50:
           #keeping tracking of how many times exactly 50 heads occured
           #in order to get the probability
           prob = prob + 1
           tp = prob / 100000
           
    print("Final probability p = {:1}".format(tp))

#main function
def main():
    coinFlip()

if __name__ == "__main__":
    main()