import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt
import string

#doing experiment using list of size m = 80000
def hacker():
    m = 80000
    count_m = 0
    #does it 1000 times
    for p in range(0,1000):
        myWord = password()
        test = createList(m)
        #if password on list, mark it as a  success and count up total successes
        if myWord in test:
            count_m = count_m + 1
    prob = count_m/1000
    print("Probabilty of password matching on list of size m is p = {:1}".format(prob))

#doing experiment using list of size k*m m = 80000, k = 7
def hacker2():
    count_mk = 0
    m = 80000*7
    #does it 1000 times
    for p in range(0,1000):
        myWord = password()
        test = createList(m)
        #if password on list, mark it as a  success and count up total successes
        if myWord in test:
            count_mk = count_mk + 1
    prob = count_mk / 1000
    print('Probability of password matching on list of m*k is p = {:1}'.format(count_mk))  

#doing experiment to figure out when p = 0.5
def hacker3():
    count_t = 0
    m = 45500*7
    #does it 1000 times
    for l in range(0, 1000):
        myWord = password()
        test = createList(m)
        #if password on list, mark it as a  success and count up total successes
        if myWord in test:
            count_t = count_t + 1    
    prob = count_t / 1000
    print("Using 45,550 to get p = 0.5 gets probability of p = {:1}".format(prob))

#creates list of size m words 
def createList(m):
    s = []
    for i in range(0,m):
        letter = string.ascii_lowercase
        a = random.choice(letter)
        b = random.choice(letter)
        c = random.choice(letter)
        d = random.choice(letter)
        word = a+b+c+d
        s.append(word)
    return s

#creates one password to be checked against a list of words
def password():
    letter = string.ascii_lowercase
    a = random.choice(letter)
    b = random.choice(letter)
    c = random.choice(letter)
    d = random.choice(letter)
    myWord = a+b+c+d
    return myWord

#main function
def main():
    hacker()
    hacker2()
    hacker3()

if __name__ == "__main__":
    main()