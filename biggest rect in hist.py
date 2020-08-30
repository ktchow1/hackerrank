# Given a histogram, find the maximum rectangle

# Method 1 in O(N^2)
def max_rect_in_hist1(hist) :
    # main-problem   = maximum(subproblems)
    # subproblems[n] = maximum retangle starting from hist[n]
    max_rect_area  = 0
    max_rect_start = 0
    
    for n in range(len(hist)) :
        rect_area   = hist[n]
        rect_height = hist[n]
        
        for m in range(n+1, len(hist)) :
            if hist[m] < rect_height : rect_height = hist[m]
            temp = rect_height * (m-n+1)
            if temp > rect_area : rect_area = temp
        if rect_area > max_rect_area :
            max_rect_area = rect_area
            max_rect_start = n
    return (max_rect_start, max_rect_area)


# Method 2 in O(N) [degenerate to O(N^2) for monotonic increasing hist]
def max_rect_in_hist2(hist) :
    max_rect_area  = 0
    max_rect_start = 0
    stack = [[0, hist[0]]]
    for m in range(1,len(hist)) :
        n =-1
        
        # [Part1] area from n to m-1, where n<m
        while len(stack) > 0 and hist[m] < stack[-1][1] :
            n,hn = stack.pop(-1)
            area = hn * (m-n) # BUG : use "hn" instead of "hist[n]", as it changes across iteration
            if area > max_rect_area :
                max_rect_area = area
                max_rect_start = n

        # BUG : Don't miss this!!!
        if n>-1 : stack.append([n, hist[m]]) 
        stack.append([m, hist[m]])
    #   print('stack:', stack, ' area:', max_rect_area, ' n:', max_rect_start)

    # [Part2] pop until empty
    while len(stack) > 0 :
        n,hn = stack.pop(-1)
        area = hn * (len(hist)-n)
        if area > max_rect_area :
            max_rect_area = area
            max_rect_start = n
    return (max_rect_start, max_rect_area)


# Consider hist having one or more local maxima
# if hist[n] is on the rising edge of hist and
# if hist[m] is on the falling edge of hist and, where n<m
# if hist[n] == hist[m] <= hist[k] for all k in [n,m], then :
# then subproblem[n] should not be continued beyond m
# since they are already covered by subproblem[n-1] or subproblem[n-2] or ...
# 
# i.e.    max_rect_in_hist2([1,3,4,2,5,3,1])
# == max( max_rect_in_hist2([0,3,4,0,0,0,0]),
#         max_rect_in_hist2([1,2,2,2,5,3,1]) )
# == max( max_rect_in_hist2([0,3,4,0,0,0,0]),
#         max_rect_in_hist2([0,0,0,0,5,3,0]),
#         max_rect_in_hist2([1,2,2,2,3,3,1]) ) 
# == max( max_rect_in_hist2([0,3,4,0,0,0,0]),
#         max_rect_in_hist2([0,0,0,0,5,3,0]),
#         max_rect_in_hist2([0,2,2,2,3,3,0]),
#         max_rect_in_hist2([1,1,1,1,1,1,1]) ) 
#
# Thus we use a stack to collect a set of ongoing subproblems in LIFO manner. Why LIFO?
# Since subproblem[n] must be push-in latter than subproblem[n-1]
# while subproblem[n] must be pop-out eariler than subproblem[n-1]
# calculation of rectangle area is done whenever a subproblem is popped only.

"""
For example, given a histogram like LHS, the processing order is in RHS :

  xx            11
 xxx  xx       222  44
 xxxx xxx      3333 555
 xxxxxxxx      66666666
xxxxxxxxxxx   77777777777    which is basically a stack
"""

print(max_rect_in_hist1([1,2,3,4,5,6]))
print(max_rect_in_hist2([1,2,3,4,5,6]))
print(max_rect_in_hist1([1,2,2,1,7,1]))
print(max_rect_in_hist2([1,2,2,1,7,1]))
print(max_rect_in_hist1([1,2,2,1,1,1,2,2,2,1])) 
print(max_rect_in_hist2([1,2,2,1,1,1,2,2,2,1]))
print(max_rect_in_hist1([4,3,2,1,5,6,7,0,8,7]))
print(max_rect_in_hist2([4,3,2,1,5,6,7,0,8,7]))
print(max_rect_in_hist1([9,9,8,22,10,16,24,6,23,18])) 
print(max_rect_in_hist2([9,9,8,22,10,16,24,6,23,18]))

num_correct = 0
import numpy
for test in range(100) :
    x = list(numpy.random.randint(0,30,100))
    y = max_rect_in_hist1(x)
    z = max_rect_in_hist2(x)
    if y[1] == z[1] : num_correct = num_correct + 1
    print('test : ', num_correct, '/', test+1)
    


    
    
    

