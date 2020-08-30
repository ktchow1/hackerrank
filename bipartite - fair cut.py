# Given arr of values, partition into two sets :
# one set contains k values
# another contains len(arr)-k values
# minimise the difference, which is defined as
#
# diff = sum_i_in_set0 :
#            sum_j_in_set1 :
#                abs(arr[i]-arr[j])
#
# This exhaustive search aims at introducing python-syntax :
# (1) combination tools
# (2) nested-list-comprehension
# (3) map and lambda

def fair_cut_exhaustive_search(k, arr):
    min_dist = float('inf')
    
    dist = [[abs(x-y) for x in arr] for y in arr]
    combos = itertools.combinations(range(len(arr)), k)
    for combo in combos :        
        sub_dist = [[dist[y][x] for x in set(range(len(arr)))-set(combo)] for y in combo]        
        temp = sum(map(sum, sub_dist))
        if (temp < min_dist) : min_dist = temp
    return min_dist

"""
(1) combinations(list, k) generates an iterable object (but not a list), for example if k = 3, it returns
    { [ list[0],list[1],list[2] ],
      [ list[0],list[1],list[3] ],
      ...
      [ list[N-3],list[N-2],list[N-1] ]}
(2) nested-list-comprehension helps to construct submatrix
(3) sum of list-of-list cannot be done by sum(sum(list_of_list)), map and lambda are needed
"""

# Here is a greedy approach in discussion forum :
# It is an intuition from physics.
# (1) generate a string of alternative 1010101, including k '1's
# (2) move the string as closed to the middle ('0's outside the string)
# That is the answer. Lets check ...
