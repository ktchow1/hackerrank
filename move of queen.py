# Given grid size nxn
# row index = y-coord = [1,n]
# col index = x-coord = [1,n]
# list of obstacles, find number of possible next-move for queue in O(N)

def queensAttack(n, k, r_q, c_q, obstacles): # k is len(obstacles), it is redundant  
    left  = 1 # use col-index
    right = n # use col-index
    lower = 1 # use row-index
    upper = n # use row-index

    # use col-index for the following
    ll = c_q - (r_q - 1)
    lr = c_q + (r_q - 1)
    ul = c_q - (n - r_q)
    ur = c_q + (n - r_q)

    if ll < 1 : ll = 1
    if lr > n : lr = n
    if ul < 1 : ul = 1
    if ur > n : ur = n

    for obstacle in obstacles :
        if obstacle[0] == r_q :
            if   obstacle[1] < c_q : left  = max(left,  obstacle[1]+1)
            elif obstacle[1] > c_q : right = min(right, obstacle[1]-1)
            else : return -1 # obstacle on queen
        elif obstacle[1] == c_q :
            if   obstacle[0] < r_q : lower = max(lower, obstacle[0]+1)
            elif obstacle[0] > r_q : upper = min(upper, obstacle[0]-1)
            else : return -1 # obstacle on queen
        elif obstacle[0]-r_q == obstacle[1]-c_q:
            if   obstacle[1] < c_q : ll = max(ll, obstacle[1]+1)
            elif obstacle[1] > c_q : ur = min(ur, obstacle[1]-1)
            else : return -1 # obstacle on queen
        elif obstacle[0]-r_q == -(obstacle[1]-c_q):
            if   obstacle[1] < c_q : ul = max(ul, obstacle[1]+1)
            elif obstacle[1] > c_q : lr = min(lr, obstacle[1]-1)
            else : return -1 # obstacle on queen
        
    count = 0
    count = count + (c_q - ll)    + (lr    - c_q)
    count = count + (c_q - ul)    + (ur    - c_q)
    count = count + (c_q - left)  + (right - c_q)
    count = count + (r_q - lower) + (upper - r_q)
    return count    
