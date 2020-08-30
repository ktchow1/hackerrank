# However the following cannot pass all test cases as it violates time limit.

def longest_common_subsequence(s1, s2):
    counts = [[0]*len(s2) for x in s1]

    # corner case
    if s1[0] == s2[0] : counts[0][0] = 1

    # 1st col
    for n in range(1,len(s1)) :
        if s1[n] == s2[0] : counts[n][0] = 1
        else : counts[n][0] = counts[n-1][0]

    # 1st col
    for n in range(1,len(s2)) :
        if s1[0] == s2[n] : counts[0][n] = 1
        else : counts[0][n] = counts[0][n-1]

    # general case
    for n in range(1,len(s1)) :
        for m in range(1,len(s2)) :
            if s1[n] == s2[m] : counts[n][m] = counts[n-1][m-1] + 1
            else : counts[n][m] = max(counts[n-1][m], counts[n][m-1])
    
    return counts[len(s1)-1][len(s2)-1]

