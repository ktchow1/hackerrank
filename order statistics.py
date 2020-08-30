def order_stat(vec, k) :
    front = 0
    back = len(vec)-1
    while front != back :
        i = front
        j = back
        while i!=j :
            if vec[i] <= vec[j] : j = j-1
            else :
                temp = vec[i]
                vec[i] = vec[j]
                vec[j] = vec[i+1]
                vec[i+1] = temp
                i = i+1

        # instead of calling recursively ...
        # quick_sort(vec[:i])
        # quick_sort(vec[i+1:])

        n = i # n = j
        if k == n : return vec[n]
        elif k < n : back = n-1           
        else : front = n+1
    return vec[front]

###############
### Testing ###
###############
import numpy
num_correct = 0
for time in range(20) :
    k = 300
    vec = numpy.random.randint(-2000, 2000, size = 500)
    ans = order_stat(vec, k)
    vec.sort()
    ANS = vec[k]
    if ans == ANS : num_correct = num_correct + 1
    print(ans, ANS)
print('num_correct ', num_correct)
    
