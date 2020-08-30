# My answer is method 2, which is the worst.
# MY lesson is :
# (1) try exhaustive search, at least it gets some marks
# (3) try google for useful properties


### Method 1 : Very slow ###
def factorial_remainder1(n):    
    count = 1
    value = 1
    for m in range(2,n+1) :
        value = value * (m-1)
        if value % m == m-1 : count = count+1
    return count

### Method 2 : Faster, but cannot handle big number division (so even worse) ###
import math
def factorial_remainder2(n):    
    x = 1
    N_old = 1
    R_old = 0 
    count = 1

    # Lets update  N and R iteratively 
    for x in range(2,n+1) :
        N_new =  N_old * x + R_old + math.floor((N_old * (-2*x+1) - R_old) / x)
        R_new = (N_old * (-2*x+1) - R_old) % x
        N_old = N_new
        R_old = R_new
        if R_new == x-1 : count = count + 1
    return count

### Method 3 : William theorem (equivalent to counting prime) ###
def factorial_remainder3(n):    
    prime = [1]*n
    for m in range(2,n) :
        x = m
        while x <= n-m :
            x = x + m
            prime[x-1] = 0
    return sum(prime)



### Test ###
for n in range(1,35) :
    print(n, end = ' ')
    print(factorial_remainder1(n), end = ' ')
    print(factorial_remainder2(n), end = ' ') 
    print(factorial_remainder3(n), end = ' ')
    if factorial_remainder2(n) != factorial_remainder3(n) :
           print('not matched')
    else : print('ok')

print('')
print(100, factorial_remainder1(100), factorial_remainder3(100))
print(300, factorial_remainder1(300), factorial_remainder3(300))
print(1000, factorial_remainder1(1000), factorial_remainder3(1000))
print(3000, factorial_remainder1(3000), factorial_remainder3(3000))
print(10000, factorial_remainder1(10000), factorial_remainder3(10000))




