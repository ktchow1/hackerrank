# Given list of strings G as input matrix of characters
# given list of strings P as template matrix of characters
# return true if P can be found inside G

def check_pattern(G, P, n, m) :
    for x in range(1,len(P)) :
        if G[n+x][m:m+len(P[x])] != P[x] : return False
    return True

def gridSearch(G, P):
    for n in range(len(G)-len(P)+1) :        
        m = 0
        while True :
            m = G[n].find(P[0], m)
            if m == -1 : break
            if (check_pattern(G, P, n, m)) : return 'YES'
            m = m + 1
            if m > len(G[n])-len(P[0]) : break
    return 'NO'
