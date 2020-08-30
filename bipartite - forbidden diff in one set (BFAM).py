"""
Given a list of integers 1,2,3,4 ... N
find the size of maximum subset, such that
no two elements in the subset differ by :
disallowed_diff[0],
disallowed_diff[1],
disallowed_diff[2] ...

This is a question from BFAM, the original question specifies :
N=13, disallowed_diff = [5,8].
"""

# My solution is an exhaustive search by building a multipartite graph
# with time  = size of subset
# with layer = { subset0, subset1, subset2, ... }, where all subsets have size equal to layer-index
# in fact, we just need to keep this layer and next layer only, instead of storing the whole graph

def fulfill_constraint(subset, n) :
    for x in subset :
        if x == n : return False
        if abs(x-n) == 5 : return False
        if abs(x-n) == 8 : return False
    return True

# This is a recombining tree, better to be implemented as set-of-set, saving time.
# However Python does not support set of set, perhaps C++ is better.
# Consider two subsets in the 5th layer (1,4,5,8,9) and (9,8,5,4,1),
# they should be considered as the same node, otherwise a waste of time.

def max_subset_no_specific_diff_allowed(N, disallowed_diff) :
    layer = set()
    layer.add(()) # empty tuple
    max_layer = 0
    max_subset = 0
     
    for n in range(1,N+1) :
        new_layer = set()
        for subset in layer : # subset is a tuple
            for m in range(1,N+1) :
                if fulfill_constraint(subset, m) :
                    temp = list(subset + (m,))
                    temp.sort()
                    new_subset = tuple(temp)
                    new_layer.add(new_subset)
                    if len(new_subset) > max_subset : max_subset = len(new_subset)
        
        layer = new_layer
        # print('\n[layer', n, ']\n', layer, '\n')        
        if len(layer) > max_layer : max_layer = len(layer)
        if len(layer) == 0 : break
    return max_layer, max_subset 

print(max_subset_no_specific_diff_allowed(13, [5,8]))
print(max_subset_no_specific_diff_allowed(20, [5,8]))



"""
BFAM's possible answer (my speculation)
I guess they do not expect an algorithmic answer for general N case,
instead they may expect a deduction method specificially for N=13 and [5,8]
This is greedy algorithm (instead of my exhaustive search).

if  1 is  included in our set, then  1+5= 6 and 1+8=9 are forbidden      ... [1]            [6,9]
as  9 is forbidden in our set, then  9-5= 4 can be included in our set   ... [1,4]          [6,9]
as  4 is  included in our set, then  4+5= 9 and 4+8=12 are forbidden     ... [1,4]          [6,9,12]
as 12 is forbidden in our set, then 12-5= 7 can be included in our set   ... [1,4,7]        [6,9,12]
as  7 is  included in our set, then  7-5= 2 and 7+5=12 are forbidden     ... [1,4,7]        [2,6,9,12]
as  2 is forbidden in our set, then  2+8=10 can be included in our set   ... [1,4,7,10]     [2,6,9,12]
as 10 is  included in our set, then 10-8= 2 and 10-5=5 are forbidden     ... [1,4,7,10]     [2,5,6,9,12]
as  5 is forbidden in our set, then  5+8=13 can be included in our set   ... [1,4,7,10,13]  [2,5,6,9,12]
as 13 is  included in our set, then 13-8= 5 and 13-5=8 are forbidden     ... [1,4,7,10,13]  [2,5,6,8,9,12]
as  8 is forbidden in our set, then  8-5= 3 can be included in our set   ... [1,3,4,7,10,13][2,5,6,8,9,12]
as  3 is  included in our set, then  3+5= 8 and 3+8=11 are forbidden     ... [1,3,4,7,10,13][2,5,6,8,9,11,12]

We can retry with another initial number instead of 1,
by following similar logic, we can derive another subset with size 6.
"""












