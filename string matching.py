# s = string
# t = template

# Method 1 runs in O(N^2)
def string_match_ON2(s, t) :
    result = []
    n = 0
    m = 0

    while n!= len(s) :
        if s[n] == t[m] :
            # case 1 : start of a match
            n = n+1
            m = m+1
            # case 2 : end of a full-match (done)
            if m == len(t) :
                result.append(n-m)
                n = n-m+1
                m = 0
        # case 3 : end of a partial-match (fail)
        elif m > 0 : 
            n = n-m+1
            m = 0
        # case 4 : just a usual mismatch
        else :
            n = n+1
            m = 0
    return result
                
"""
There are 4 cases with difference updating equations for n&m.
It is not a must for case 2&3 to go all the way back to n-m+1.
----------------------------------------------------------------------------
Consider a template with all unique characters :
 
    0123456789 
s = xxxxabcxxxxxxxxxxx
t =     abcde
n = 7
m = 3

There is no need to go back to (n=5,m=0), since
s[5]==t[1]!=t[0]='a'
s[6]==t[2]!=t[0]='a'
so we can retry with (n=7,m=0) 
----------------------------------------------------------------------------
Consider a template with repeated pattern :
 
    0123456789 
s = xxxxabcabxxxxxxxxxx
t =     abcabde
n = 9
m = 5

There is no need to go back to (n=5,m=0), since
s[5]==t[1]!=t[0]=='a'
s[6]==t[2]!=t[0]=='a'
however we cannot retry with (n=9,m=0), since
s[7]==t[3]==t[0]=='a'
s[8]==t[4]==t[1]=='b'
so we have to retry with (n=9,m=2)
----------------------------------------------------------------------------
We need a preprocessing to calculate backtrace[m], so that we update by :
n = no_update, always move forward, i.e. no duplicated comparison
m = backtrace[m]
len(backtrace) = len(template)+1 (why plus 1? see case 2 below)
----------------------------------------------------------------------------"""

# Method 2 runs in O(N), called KMP-algo
def construct_backtrace(t) :

    # case A : failure after partial match leads to (n=unchanged, m=0) in general
    backtrace = [0] * (len(t)+1)
    backtrace[0] = None

    # case B : failure on t[m], where t[:m-1] repeats in template 
    for shift in range(1, len(t)-1) :
        # after this loop, m denotes number of self-repeating characters
        for m in range(0, len(t)-shift) :
            if t[m] != t[m+shift] : break 
        else : m = len(t)-shift
        backtrace[m+shift] = max(backtrace[m+shift], m)
        
    return backtrace

def string_match_KMP(s, t) :
    backtrace = construct_backtrace(t)
    result = []
    n = 0
    m = 0    

    while n!= len(s) :
        if s[n] == t[m] :
            # case 1 : start of a match
            n = n+1
            m = m+1
            # case 2 : end of a match (success)
            if m == len(t) :
                result.append(n-m)
            #   n = n
                m = backtrace[m]
        # case 3 : end of a partial match (fail)
        elif m > 0 : 
        #   n = n
            m = backtrace[m]
        # case 4 : a usual mismatch
        else : 
            n = n+1
            m = 0
    return result


print(string_match_ON2("xxxaaaaxxxxxaaaaaaxxxxxxxx", "aaa"))
print(string_match_KMP("xxxaaaaxxxxxaaaaaaxxxxxxxx", "aaa")) 
print(string_match_ON2("abcxxxxxxxababcabxxxababababcxxxxx", "abc"))
print(string_match_KMP("abcxxxxxxxababcabxxxababababcxxxxx", "abc")) 
print(string_match_ON2("abcxxxxxxxababcabxxxababababcxxxxx", "ababc"))
print(string_match_KMP("abcxxxxxxxababcabxxxababababcxxxxx", "ababc"))
print(string_match_ON2("abcxxxxxxxababcabxxxababababcxxxxx", "abababc"))
print(string_match_KMP("abcxxxxxxxababcabxxxababababcxxxxx", "abababc"))


# examples from wiki
print('backtrace = ', construct_backtrace('abcdabd'))
print('backtrace = ', construct_backtrace('abacababc'))
print('backtrace = ', construct_backtrace('abacababa'))
print('backtrace = ', construct_backtrace('participate in parachute'))

import random
num_correct = 0
for test in range(1000) :
    s = ''.join([random.choice('abc') for i in range(1000)])
    t = ''.join([random.choice('abc') for i in range(40)])
    ans0 = string_match_ON2(s,t)
    ans1 = string_match_ON2(s,t)
    if ans0 == ans1 : num_correct = num_correct + 1
    print('num=', num_correct, '/', test+1, construct_backtrace(t))
#   print('num=', num_correct, '/', test+1, ' s=', s, 't=', t)
    
    





