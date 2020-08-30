"""
Given an array and a number k
find the number of pairs (n,m) such that

(array[n] + array[m]) % k = 0
"""

# [3 steps in two lines, woo its like mapreduce]
# input    : list comprehension is for constructing list or matrix for mapreduce
# mapping  : map (lambda, list) is for conversion from matrix to another with same size
# reducing : function sum(list) is for summarising result

def count_divisible_sum_pairs(K, array):
    temp = [array[i]+array[j] for i in range(len(array)) for j in range(i+1, len(array))] 
    return sum(map(lambda x : not x % K, temp))
