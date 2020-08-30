# Given vector v0 and v1
# find x0 in v0 and
# find x1 in v1
# such that x0+x1 is closest to target
import random

# O(N^2) search, no sorting is needed
def nearest_target_sum0(v0,v1,target) :
    min_dist = float('inf')
    opt_x0 = 0
    opt_x1 = 0

    for x0 in v0 :
        for x1 in v1 :
            if abs(x0+x1-target) < min_dist :
                min_dist = abs(x0+x1-target)
                opt_x0 = x0
                opt_x1 = x1
    return [opt_x0, opt_x1]

# O(N) search and O(NlogN) sorting    
def nearest_target_sum1(v0,v1,target) :
    v0.sort() # Don't forget sorting. 
    v1.sort() 

    min_dist = float('inf')
    opt_x0 = 0
    opt_x1 = 0

    n0 = len(v0)-1
    n1 = 0
    while True :
        # this location
        if abs(v0[n0]+v1[n1]-target) < min_dist :
            min_dist = abs(v0[n0]+v1[n1]-target)
            opt_x0 = v0[n0]
            opt_x1 = v1[n1]

        # next location
        if   v0[n0]+v1[n1] == target : return [opt_x0, opt_x1]
        elif v0[n0]+v1[n1] < target :
            n1 = n1 + 1
            if n1==len(v1) : return [opt_x0, opt_x1]
        else :
            n0 = n0 - 1
            if n0<0 : return [opt_x0, opt_x1]


v0 = random.sample(range(1,100), 10)
v1 = random.sample(range(1,100), 10)
y0 = nearest_target_sum0(v0,v1,80)
y1 = nearest_target_sum1(v0,v1,80)
print(y0, 'sum=', sum(y0))
print(y1, 'sum=', sum(y1))


