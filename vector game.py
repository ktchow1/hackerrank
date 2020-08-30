def max_profit0(vec) : # O(N^2) exhaustive search
    ans = -float('inf')
    for n in range(len(vec)) :
        for m in range(n+1, len(vec)) :
            if vec[m]-vec[n] > ans : ans = vec[m]-vec[n]
    return ans

def max_profit1(vec) : # O(N) dynamic programming 
    sub = vec[1]-vec[0]
    ans = sub     
    for n in range(2, len(vec)) :
        sub = max(sub+vec[n]-vec[n-1], vec[n]-vec[n-1])
        ans = max(ans, sub)
    return ans

def max_profit2(vec) : # O(NlogN) divide and conquer   
    if len(vec) == 1 : return -float('inf')    
    mid = int(len(vec)/2)
    v0  = min(vec[:mid])
    v1  = max(vec[mid:])
    return max(max_profit2(vec[:mid]), max_profit2(vec[mid:]), v1-v0)

def target_diff(vec, target) : # O(N) dynamic programming
    hist = {}
    ans = 0
    for n in range(len(vec)) :
        # task 1 : O(1) search in hist 
        if target-vec[n] in hist : ans = ans + hist[target-vec[n]]
        
        # task 2 : construct hist on the run
        if vec[n] in hist : hist[vec[n]] = hist[vec[n]] + 1
        else : hist[vec[n]] = 1
    return ans

def max_subseq_sum0(vec) : # O(N^2) exhaustive search
    ans = -float('inf')
    for n in range(len(vec)) :
        cum = 0
        for m in range(n, len(vec)) :
            cum = cum + vec[m]
            ans = max(ans, cum)
    return ans
    
def max_subseq_sum1(vec) : # O(N) dynamic programming (Kadane algorithm)
    sub = vec[0]
    ans = sub 
    for n in range(1, len(vec)): 
        sub = max(sub + vec[n], vec[n])
        ans = max(ans, sub)
    return ans

def max_subseq_sum2(vec) : # O(NlogN) divide and conquer
    if len(vec) == 1 : return vec[0]
    mid  = int(len(vec)/2)
    
    cum0 = vec[mid-1]
    ans0 = vec[mid-1]
    for n in range(mid-2,-1,-1) :
        cum0 = cum0 + vec[n]
        ans0 = max(ans0, cum0)

    cum1 = vec[mid]
    ans1 = vec[mid]
    for n in range(mid+1, len(vec)) :
        cum1 = cum1 + vec[n]
        ans1 = max(ans1, cum1)
            
    return max(max_subseq_sum2(vec[:mid]), max_subseq_sum2(vec[mid:]), ans0 + ans1)
      
def count_zero_subseq_sum(vec) : # <O(N^2) cannot generalize to non-zero target
    sub = [0]*len(vec)
    for n in range(len(vec)-1,-1,-1) :
        cum = 0
        for m in range(n, len(vec)) :
            cum = cum + vec[m]
            if cum == 0 :
                if m+1 < len(vec) :
                       sub[n] = 1 + sub[m+1]
                else : sub[n] = 1
                break
    return sum(sub)

def count_target_subseq_sum0(vec, target) : # O(N^2) exhaustive search
    ans = 0
    for n in range(len(vec)) :
        cum = 0
        for m in range(n, len(vec)) :
            cum = cum + vec[m]
            if cum == target : ans = ans + 1
    return ans

def count_target_subseq_sum1(vec, target) : # O(N) dynamic programming       
    cum  = 0
    hist = {}
    ans  = 0
    for n in range(len(vec)) :
        cum = cum + vec[n]
        
        # task 1 : O(1) search in hist 
        if cum == target : ans = ans + 1 # Don't forget this case
        if cum-target in hist : ans = ans + hist[cum-target]
        
        # task 2 : construct hist on the run     
        if cum not in hist :
               hist[cum] = 1
        else : hist[cum] = hist[cum] + 1        
    return ans

def longest_target_subseq_sum0(vec, target) : # O(N^2) exhaustive search
    ans = 0
    for n in range(len(vec)) :
        cum = 0
        for m in range(n, len(vec)) :
            cum = cum + vec[m]
            if cum == target :
                if ans < m-n+1 : ans = m-n+1
    return ans

def longest_target_subseq_sum1(vec, target) : # O(N) dynamic programming       
    cum  = 0
    hist = {}
    ans  = 0
    # do two things in parallel (like passing car)
    for n in range(len(vec)) :
        cum = cum + vec[n]
        
        # task 1
        if cum == target : ans = ans + 1 # This case must be the longest
        elif cum-target in hist : 
            if ans < n-hist[cum-target] : ans = n-hist[cum-target]
        
        # task 2        
        if cum not in hist : hist[cum] = n
        else : pass # just need to record the first index
    return ans

def count_div_by_target_subseq_sum(vec, target) :
    cum  = 0
    hist = {}                
    ans  = 0                
    for n in range(len(vec)) :
        cum = cum + vec[n]
        tmp = cum % target

        # merge task 1&2, avoid repeated calculation with tmp
        if tmp == 0 : ans = ans + 1
        if tmp in hist : 
            ans = ans + hist[tmp]
            hist[tmp] = hist[tmp] + 1
        else : hist[tmp] = 1                
    return ans

def max_subseq_prod(vec):
    sub0 = vec[0]
    sub1 = vec[0]
    ans  = vec[0]
    for n in range(1, len(vec)) :  
        tmp0 = sub0 * vec[n]
        tmp1 = sub1 * vec[n]
        sub0, sub1 = max(tmp0, tmp1, vec[n]), min(tmp0, tmp1, vec[n])
        ans  = max(ans, sub0)            
    return ans

def count_less_than_target_subseq_product(vec, target):
    if target == 0 : return 0
    if target == 1 : return 0  
    cum = 1
    idx = 0    
    ans = 0
    for n in range(len(vec)) :
        cum = cum * vec[n]
        while cum >= target : 
            cum = cum / vec[idx]
            idx = idx+1
        ans = ans + (n-(idx-1))
    return ans

def longest_non_repeat_string0(vec) :
    ans = 0
    for n in range(len(vec)) :
        for m in range(n, len(vec)) :
            unique_set = set()
            for k in range(n,m+1) :
                if vec[k] in unique_set : break
                unique_set.add(vec[k])
            ans = max(ans, len(unique_set))                    
    return ans

def longest_non_repeat_string1(vec) :
    hist = {}
    sub = 0
    ans = 0
    for n in range(len(vec)) :
        if vec[n] in hist : 
               sub = min(sub+1, n-hist[vec[n]])
        else : sub = sub+1             
        ans = max(ans, sub)
        hist[vec[n]] = n       
    return ans

'''
Pass most cases, but doesn't work for cycles
cycle with period 0 AAAAAAAAA works
cycle with period 1 ABABABABA doesn't
cycle with period 2 ABCBABCBA doesn't
to fix it, need O(N^2)
or use "Manachar algorithm" in O(N)
'''
def longest_palindrome(s):
    in0 = 0 # start of constant for previous subproblem
    in1 = 0 # start of palindrome for previous subproblem        
    ans = [0,0]                        
    for n in range(1,len(s)) :
        if s[n] != s[n-1] : in0 = n
                         
        if in1>=1 and s[n] == s[in1-1] : in1 = in1-1
        else : in1 = in0
            
        if n-(in0-1) > ans[1]-(ans[0]-1) : ans = [in0,n]
        if n-(in1-1) > ans[1]-(ans[0]-1) : ans = [in1,n]
    return s[ans[0]:ans[1]+1]

def longest_palindrome2(s) : # exhaustive search
    ans = [0,0]
        
    # odd palindrome
    for n in range(len(s)) :
        m = 0
        while True :
            if n-m-1 < 0 : break
            if n+m+1 >= len(s) : break
            if s[n-m-1] != s[n+m+1] : break
            m = m+1                
        if 2*m+1 > ans[1]-ans[0]+1 : ans = [n-m,n+m]
             
    # even palindrome
    for n in range(1,len(s)) :
        m = 0
        while True :
            if n-m-1 < 0 : break
            if n+m >= len(s) : break
            if s[n-m-1] != s[n+m] : break
            m = m+1
        if 2*m > ans[1]-ans[0]+1 : ans = [n-m,n+m-1]
                                                               
    return s[ans[0]:ans[1]+1]

def shortest_unsorted_subseq0(nums): # O(NlogN), using sorting 
    sorted_nums = list(nums)
    sorted_nums.sort()                
        
    for n in range(len(nums)) :
        if nums[n] != sorted_nums[n] : break
    else : return 0
    for m in range(len(nums)-1,-1,-1) :
        if nums[m] != sorted_nums[m] : break
    else : return 0       
    return m-n+1

''' like biggest-rect, turn out slower than above '''
def shortest_unsorted_subseq1(nums): # O(N), using stack 
    sz0 = len(nums)
    sz1 = len(nums)
    ### forward ###    
    s = []        
    for n in range(len(nums)) :            
        while len(s) > 0 and nums[n] < s[-1] : 
            s.pop(-1)
            if sz0 > len(s) : sz0 = len(s)
        s.append(nums[n])
    if sz0 == len(nums) : return 0
    ### backward ###
    s = []        
    for n in range(len(nums)-1,-1,-1) : 
        while len(s) > 0 and nums[n] > s[-1] : 
            s.pop(-1)
            if sz1 > len(s) : sz1 = len(s)
        s.append(nums[n])
    if sz1 == len(nums) : return 0                           
    return len(nums)-sz0-sz1

        
#########################
### Testing functions ###
#########################
import time
import numpy

def test_dist_sum() :
    pass

def test_max_profit(num_test, vec_size) :
    num_done, num_corr = 0,0
    for test in range(num_test) :
        vec  = list(numpy.random.randint(-1000, 1000, size=vec_size))
        ans0 = max_profit0(vec)
        ans1 = max_profit1(vec)
        ans2 = max_profit2(vec)

        num_done = num_done + 1
        if ans0 == ans1 and ans0 == ans2 : num_corr = num_corr + 1
        print(test, ans0, ans1, ans2)
    return [vec_size, num_corr, num_done]

def test_max_subseq_sum(num_test, vec_size) :
    num_done, num_corr = 0,0
    for test in range(num_test) :
        vec  = list(numpy.random.randint(-100, 100, size=vec_size))
        ans0 = max_subseq_sum0(vec)
        ans1 = max_subseq_sum1(vec)
        ans2 = max_subseq_sum2(vec)

        num_done = num_done + 1        
        if ans0 == ans1 and ans0 == ans2 : num_corr = num_corr + 1
        print(test, ans0, ans1, ans2)
    return [vec_size, num_corr, num_done]

def test_zero_subseq_sum(num_test, vec_size) :
    num_done, num_corr = 0,0
    for test in range(num_test) :
        vec  = list(numpy.random.randint(-100, 100, size=vec_size))
        ansX = zero_subseq_sum(vec)
        ans0 = target_subseq_sum0(vec, 0)
        ans1 = target_subseq_sum1(vec, 0)        

        num_done = num_done + 1
        if ansX == ans0 and ansX == ans1 : num_corr = num_corr + 1        
        print(test, ansX, ans0, ans1)
    return [vec_size, num_corr, num_done]

def test_longest_target_subseq_sum(num_test, vec_size) :
    num_done, num_corr = 0,0
    for test in range(num_test) :
        vec  = list(numpy.random.randint(-100, 100, size=vec_size))
        ans0 = longest_target_subseq_sum0(vec, 0)
        ans1 = longest_target_subseq_sum1(vec, 0)        

        num_done = num_done + 1
        if ans0 == ans1 : num_corr = num_corr + 1        
        print(test, ans0, ans1)
    return [vec_size, num_corr, num_done]

def test_longest_non_repeat_string(num_test, vec_size) :
    num_done, num_corr = 0,0
    for test in range(num_test) :
        vec  = list(numpy.random.randint(0, 15, size=vec_size))
        ans0 = longest_non_repeat_string0(vec)
        ans1 = longest_non_repeat_string1(vec)        

        num_done = num_done + 1
        if ans0 == ans1 : num_corr = num_corr + 1        
        print(test, ans0, ans1)
    return [vec_size, num_corr, num_done]
    
############
### Main ###
############
import sys
if __name__ == '__main__' :
    t = int(sys.argv[1])
    
    if t==0 :
        test_max_profit(10, 100)
        test_max_profit(10, 400)        

    elif t==1 :
        test_max_subseq_sum(10, 100)
        test_max_subseq_sum(10, 2000)
    
    elif t==2 : 
        test_zero_subseq_sum(10, 200)
        test_zero_subseq_sum(10, 1000)

    elif t==3 : 
        test_longest_target_subseq_sum(10, 200)
        test_longest_target_subseq_sum(10, 1000)

    elif t==4 : 
        ans = test_longest_non_repeat_string(100, 100)
        print('num_corr =', ans[1])
        print('num_done =', ans[2])
    



    
    
