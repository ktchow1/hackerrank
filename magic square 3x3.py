# Magic square is a square such that each row, each col, two diagonals share same sum.
# Given a 3x3 matrix, convert it into magic square with min cost, cost is defined as :
# cost = sum_i(sum_j(abs(A[i][j]-B[i][j]))) where A and B are the new and old squares.

"""
### Solution ###
[step 1] find property of 3x3 magic square
1.1 Considering mid-row, mid-col, two diagonals, we know that centre pixel must be 5
1.2 Considering LHS-col, RHS-col, up-row, low-row, we know that the 4 corners must be even, why?

Just think about :
|OEO|
|E5E| is invalid as some sums are even, some sums are odd
|OEO|

Now there are 8 possible configurations :
UL,UR = 2,4 / 2,6 / 4,2 / 4,8 ... as shown in code

[step 2] find distance to the nearest magic square given any init square matrix
This is simply done by exhaustive search of the 8 cases.
"""

def magic_square_3x3(s) :
    min_cost = float('inf')
    for scheme in range(8) :
        if   scheme == 0 : UL,UR = 2,4
        elif scheme == 1 : UL,UR = 2,6
        elif scheme == 2 : UL,UR = 4,2
        elif scheme == 3 : UL,UR = 4,8
        elif scheme == 4 : UL,UR = 6,2
        elif scheme == 5 : UL,UR = 6,8
        elif scheme == 6 : UL,UR = 8,4
        elif scheme == 7 : UL,UR = 8,6
        LL = 10-UR
        LR = 10-UL

        cost = abs(s[1][1]-5) # centre pixel must be 5
        cost = cost + abs(s[0][0] - UL)
        cost = cost + abs(s[0][2] - UR)
        cost = cost + abs(s[2][0] - LL)
        cost = cost + abs(s[2][2] - LR)
        cost = cost + abs(s[0][1] - (15-UL-UR)) # magic const must be 15
        cost = cost + abs(s[1][0] - (15-UL-LL)) # magic const must be 15
        cost = cost + abs(s[1][2] - (15-UR-LR)) # magic const must be 15
        cost = cost + abs(s[2][1] - (15-LL-LR)) # magic const must be 15

        if cost < min_cost : min_cost = cost
    return min_cost

