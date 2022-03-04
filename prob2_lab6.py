import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt

#using initial vector all 1/5
def pagerank(p,v,n):
    #getting initial values into list 
    one = []
    one.append(v.item(0))
    two = []
    two.append(v.item(1))
    three = []
    three.append(v.item(2))
    four = []
    four.append(v.item(3))
    five = []
    five.append(v.item(4))
    #setting temp equal to initial vector
    temp = v
    #using state transition matrix approach 
    for i in range(1,n):
        #matrix mult
        a = np.matmul(temp,p)
        #setting new value equal to temp to use on next iteration
        temp = a
        #getting values at each place
        o = a.item(0)
        t = a.item(1)
        th = a.item(2)
        f = a.item(3)
        fi = a.item(4)
        #appending to list
        one.append(o)
        two.append(t)
        three.append(th)
        four.append(f)
        five.append(fi)
    #finding rank of pages
    page_a = one[-1]
    page_b = two[-1]
    page_c = three[-1]
    page_d = four[-1]
    page_e = five[-1]
    rank = [page_a,page_b,page_c,page_d,page_e]
    #min and max
    n = max(rank)
    m = min(rank)
    rank.remove(n)
    rank.remove(m)
    nn = max(rank)
    mm = min(rank)
    rank.remove(nn)
    rank.remove(mm)
    #setting value equal to page 
    #highest ranking page
    if n == page_a:
        first = 'A'
    elif n == page_b:
        first = 'B'
    elif n == page_c:
        first = 'C'
    elif n == page_d:
        first = 'D'
    elif n == page_e:
        first = 'E'

    if nn == page_a:
        second = 'A'
    elif nn == page_b:
        second = 'B'
    elif nn == page_c:
        second = 'C'
    elif nn == page_d:
        second = 'D'
    elif nn == page_e:
        second = 'E'
    #middle rank
    if rank[0] == page_a:
        third = 'A'
    elif rank[0] == page_b:
        third = 'B'
    elif rank[0] == page_c:
        third = 'C'
    elif rank[0] == page_d:
        third = 'D'
    elif rank[0] == page_e:
        third = 'E'

    if mm == page_a:
        forth = 'A'
    elif mm == page_b:
        forth = 'B'
    elif mm == page_c:
        forth = 'C'
    elif mm == page_d:
        forth = 'D'
    elif mm == page_e:
        forth = 'E'
    #lowest ranking page
    if m == page_a:
        fifth = 'A'
    elif m == page_b:
        fifth = 'B'
    elif m == page_c:
        fifth = 'C'
    elif m == page_d:
        fifth = 'D'
    elif m == page_e:
        fifth = 'E'
    print("Rank of the pages with equal intitial prob is {:1}, {:1}, {:1}, {:1}, {:1}".format(first, second, third, forth, fifth))
    
    #plotting
    fig1 = plt.figure(1)
    #lines for page A,B,C,D, and E
    plt.plot(range(20),one, linestyle = 'dashed', linewidth = 1, color = 'Blue', label = 'Page A')
    plt.plot(range(20),one,'bo')
    plt.plot(range(20),two, linestyle = 'dashed', linewidth = 1, color = 'Red', label = 'Page B')
    plt.plot(range(20),two,'ro')
    plt.plot(range(20),three, linestyle = 'dashed', linewidth = 1, color = 'Green', label = 'Page C')
    plt.plot(range(20),three,'go')
    plt.plot(range(20),four, linestyle = 'dashed', linewidth = 1, color = 'Black',label = 'Page D')
    plt.plot(range(20),four,'ko')
    plt.plot(range(20),five, linestyle = 'dashed', linewidth = 1, color = 'Magenta', label = 'Page E')
    plt.plot(range(20),five,'mo')
    legend = plt.legend(loc = 'upper right', shadow = True, ncol = 3)
    #naming
    plt.title("PageRank with Equal Initial States")
    plt.xlabel("Step Number")
    plt.ylabel("Probability")
    plt.show()

#using initial vector e is 1    
def page(p,v,n):
    #getting initial values into list 
    one = []
    one.append(v.item(0))
    two = []
    two.append(v.item(1))
    three = []
    three.append(v.item(2))
    four = []
    four.append(v.item(3))
    five = []
    five.append(v.item(4))
    #setting temp equal to initial vector
    temp = v
    #using state transition matrix approach 
    for i in range(1,n):
        #matrix mult
        a = np.matmul(temp,p)
        #setting new value equal to temp to use on next iteration
        temp = a
        #getting values at each place
        o = a.item(0)
        t = a.item(1)
        th = a.item(2)
        f = a.item(3)
        fi = a.item(4)
        #appending to list
        one.append(o)
        two.append(t)
        three.append(th)
        four.append(f)
        five.append(fi)
    #finding page rank
    #finding rank of pages
    page_a = one[-1]
    page_b = two[-1]
    page_c = three[-1]
    page_d = four[-1]
    page_e = five[-1]
    rank = [page_a,page_b,page_c,page_d,page_e]
    #min and max
    n = max(rank)
    m = min(rank)
    rank.remove(n)
    rank.remove(m)
    nn = max(rank)
    mm = min(rank)
    rank.remove(nn)
    rank.remove(mm)
    #setting value equal to page 
    #highest ranking page
    if n == page_a:
        first = 'A'
    elif n == page_b:
        first = 'B'
    elif n == page_c:
        first = 'C'
    elif n == page_d:
        first = 'D'
    elif n == page_e:
        first = 'E'

    if nn == page_a:
        second = 'A'
    elif nn == page_b:
        second = 'B'
    elif nn == page_c:
        second = 'C'
    elif nn == page_d:
        second = 'D'
    elif nn == page_e:
        second = 'E'
    #middle rank
    if rank[0] == page_a:
        third = 'A'
    elif rank[0] == page_b:
        third = 'B'
    elif rank[0] == page_c:
        third = 'C'
    elif rank[0] == page_d:
        third = 'D'
    elif rank[0] == page_e:
        third = 'E'

    if mm == page_a:
        forth = 'A'
    elif mm == page_b:
        forth = 'B'
    elif mm == page_c:
        forth = 'C'
    elif mm == page_d:
        forth = 'D'
    elif mm == page_e:
        forth = 'E'
    #lowest ranking page
    if m == page_a:
        fifth = 'A'
    elif m == page_b:
        fifth = 'B'
    elif m == page_c:
        fifth = 'C'
    elif m == page_d:
        fifth = 'D'
    elif m == page_e:
        fifth = 'E'

    print("Rank of the pages with always starting at page E is {:1}, {:1}, {:1}, {:1}, {:1}".format(first, second, third, forth, fifth))
    
    #plotting
    fig1 = plt.figure(1)
    #lines for page A,B,C,D and E
    plt.plot(range(20),one, linestyle = 'dashed', linewidth = 1, color = 'Blue', label = 'Page A')
    plt.plot(range(20),one,'bo')
    plt.plot(range(20),two, linestyle = 'dashed', linewidth = 1, color = 'Red',label = 'Page B')
    plt.plot(range(20),two,'ro')
    plt.plot(range(20),three, linestyle = 'dashed', linewidth = 1, color = 'Green', label = 'Page C')
    plt.plot(range(20),three,'go')
    plt.plot(range(20),four, linestyle = 'dashed', linewidth = 1, color = 'Black', label = 'Page D')
    plt.plot(range(20),four,'ko')
    plt.plot(range(20),five, linestyle = 'dashed', linewidth = 1, color = 'Magenta', label = 'Page E')
    plt.plot(range(20),five,'mo')
    legend = plt.legend(loc = 'upper right', shadow = True)
    #naming
    plt.title("PageRank with nonequal Initial States")
    plt.xlabel("Step Number")
    plt.ylabel("Probability")
    plt.show()

#main function
def main():
    p = np.matrix([[0,1,0,0,0],[1/2,0,1/2,0,0],[1/3,1/3,0,0,1/3],[1,0,0,0,0],[0,1/3,1/3,1/3,0]])
    v = np.matrix([[0.2,0.2,0.2,0.2,0.2]])
    v2 = np.matrix([[0,0,0,0,1]])
    n = 20
    pagerank(p,v,n)
    page(p,v2,n)

if __name__ == "__main__":
    main()