'''
Algorithms for randomly choosing k samples from a list of n items, where n is either a very large or unknown number. 
Typically n is large enough that the list doesn’t fit into main memory.

So we are given a big array (or stream) of numbers (to simplify),
and we need to write an efficient function to randomly select k numbers where 1 <= k <= n. Let the input array be stream[].
'''


import random

def selectKItems(stream, n, k):
    # From stream[0..n-1]
    reservoir = [0] * k
    for i in range(k):
        reservoir[i] = stream[i]
    
    for i in range(k, n):
        # random number between 0 and i
        r = random.randint(0, i+1)

        # if random number is smaller than k, replace the elem
        if r < k:
            reservoir[r] = stream[i]
    
    return reservoir

def main():
    stream = [0,1,2,3,4,5,6,7,8,9]
    sol = selectKItems(stream, 10, 3)
    print(sol)

main()