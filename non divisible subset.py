'''
Given a list of integers s and a number k, find max subset of s,
such that sum of any two numbers from the subset are non divisble by k.
'''


def nonDivisibleSubset(k, s):
    hist = [0]*k
    for n in s : hist[n % k] = hist[n % k] + 1    
    
    count = 0
    i = 1
    j = k-1    
    while i < j : 
        count = count + max(hist[i], hist[j])
        i = i + 1
        j = j - 1
    
    if hist[0] > 0 : count = count + 1
    if k % 2 == 0 and hist[k//2] > 0 : count = count + 1
    return count

# k//2 means floor(k/2) 
