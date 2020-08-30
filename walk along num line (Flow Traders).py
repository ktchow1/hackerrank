''' Please refer to Flow Trader document for the question. '''

####################################
### My answer (correct but slow) ###
####################################
def is_reachable(s, n0, n1, N) :
    pos = n0
    for c in s :
        if c == 'l' :
            pos = pos-1
            if pos < 0 : return False
        else :
            pos = pos+1
            if pos > N : return False
    if pos == n1 : return True
    else : return False
    
def find_substr(command, substrs) :
    if len(command) == 0 : return

    temp = set()
    find_substr(command[1:], temp)

    for s in temp :
        substrs.add(s)    
        substrs.add(command[0]+s)
    substrs.add(command[0:1]) # Dont forget this
    
def num_walk_along_num_line1(command, n0, n1, N) :
    substrs = set()
    find_substr(command, substrs)

    count = 0
    for s in substrs :
        if is_reachable(s, n0, n1, N) :
            count = count + 1
    return count

#################################################
### Answer from web (correct but even slower) ###
#################################################
def solve_recur(command, index, n0, n1, N, path, result):
    if n0 == n1 : result.add(path)
    if index == len(command) : return

    solve_recur(command, index+1, n0, n1, N, path, result)
    if command[index] == 'l':
        if n0 > 0 : solve_recur(command, index+1, n0-1, n1, N, path+'l', result)
    else :
        if n0+1 < N : solve_recur(command, index+1, n0+1, n1, N, path+'r', result)
    
def num_walk_along_num_line2(command, n0, n1, N):  
    result = set([])
    solve_recur(command, 0, n0, n1, N, '', result)
    return len(result)
    
    
print(num_walk_along_num_line1("rrlrlr", 1, 2, 6))
print(num_walk_along_num_line2("rrlrlr", 1, 2, 6))
print(num_walk_along_num_line1("rrlrllrlrlrlrrlrlrrrrlll", 1, 6, 250))
print(num_walk_along_num_line2("rrlrllrlrlrlrrlrlrrrrlll", 1, 6, 250))

    
