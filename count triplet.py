"""
Given a vector of integers, count the number of triplet
triplet is defined as a GP with size 3, i.e. a, ar, ar^2
"""


# This solution is slow, cannot get full marks
def calculate_combination(x) :
    if len(x) < 3 : return 0
    output = x[0] * x[1] * x[2]
    pro_AB = x[1] * x[2]
    pro_BC = x[2]
    for n in range(3, len(x)) : output, pro_AB, pro_BC = output + pro_AB*x[n], pro_BC*x[n], x[n]
    return output

def countTriplets(arr, r):
    output = 0

    hist = {}
    for x in arr :
        if x in hist : hist[x] = hist[x] + 1
        else : hist[x] = 1

    # Consider corner case when x=1
    if x==1 : 
        for key,value in hist.items() : output = output + value * (value-1) * (value-2) / 6
        return output

    # Consider general case
    for key in sorted(hist) :
        if hist[key] == 0 : continue
        counts, hist[key] = [hist[key]], 0
        
        rkey = key
        while True :
            rkey = r * rkey
            if rkey in hist :
                counts.append(hist[rkey])
                hist[rkey] = 0
            else : break

        output = output + calculate_combination(counts)

    return output
