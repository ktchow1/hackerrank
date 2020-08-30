#####################
### Adjacent swap ###
#####################
'''
Given a queue, q[n] is the original position of nth person, what is min(#bribes) if :
- each person can bribe the former atmost twice
- each person can be bribed inf num of times

Both methods below use bubble-sort property that :
- num of adj swaps = num of inversions 

Target is to reduce O(N^2) into O(N), by asymmetric constraint :
(1) n >= q[n]-2 
(2) for all m > n count inversion q[m] < q[n], m can be much greater than n
or  for all m < n count inversion q[m] > q[n], m cannot be smaller than n-2 
'''

# correct, slow
def minimum_bribes(q): 
    num_bribes = 0
    for n in range(len(q)) :
        if n < q[n]-2 :
            print('Too chaotic')
            return None

    for n in range(len(q)) :
        for m in range(n+1, len(q)) : 
            if q[m] < q[n] : num_bribes = num_bribes + 1
            
    print(num_bribes)

# correct, fast 
def minimum_bribes(q): 
    num_bribes = 0
    for n in range(len(q)) :
        if n < q[n]-2 :
            print('Too chaotic')
            return None

    for n in range(len(q)) :    
        for m in range(max(0, q[n]-2), n) :  
            if q[m] > q[n] : num_bribes = num_bribes + 1 

    print(num_bribes)
