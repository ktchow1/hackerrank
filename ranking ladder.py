# given a vector of recorded scores
# given a vector of Alice's scores
# return Alice's rank in the process
#
# score = 80 50 100 100 40 60 60 10
# rank  =  2  4   1   1  5  3  3  6

def climbingLeaderboard(scores, alice):
    output = []

    # [step 1] build the ladder
    ladder = [scores[0]]
    for score in scores :
        if score != ladder[len(ladder)-1] : 
            ladder.append(score)
        
    # [step 2] climb from the bottom
    index = len(ladder)-1
    rank  = len(ladder)+1

    for score in alice :
        while index>=0 :
            if score > ladder[index] : 
                rank = index+1
            elif score == ladder[index] : 
                rank = index+1
                break
            else : break
            index = index-1
            
        output.append(rank)
    return output

# If the rank definition is changed into :
# score = 80 50 100 100 40 60 60 10
# rank  =  3  6   1   1  7  4  4  8
#
# then how should we modify the above code?
