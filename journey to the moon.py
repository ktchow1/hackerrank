# Pick two men each from different countries to the moon
#
# Given N nodes and K node-pairs (two nodes in one node-pairs are linked)
# if we pick two nodes, how many combo are that if these two nodes are not connected?


def calculate_total_combo(clusters, num_unclustered_nodes) :
    # one node from each cluster
    count = 0
    for x in range(len(clusters)) :
        for y in range(x+1, len(clusters)) :
            count = count + clusters[x]*clusters[y]

    # one node from clustered, one node from unclustered
    for x in clusters :
        count = count + x*num_unclustered_nodes

    # both nodes from unclustered
    count = count + int(num_unclustered_nodes * (num_unclustered_nodes-1)/2) # int to prevent floating point
    return count

# Containers for region growing in graph:
# (1) edges (= image in ASM)
# (2) label array
# (3) region growing stack
# (4) list of clusters
def journey_to_moon(n, astronaut): 
    
    # step 1 : construct edges
    edges = {}
    for x in astronaut :
        if x[0] not in edges : 
               edges[x[0]] =  {x[1]}
        else : edges[x[0]].add(x[1])
        if x[1] not in edges : 
               edges[x[1]] =  {x[0]}
        else : edges[x[1]].add(x[0])
    
    # step 2 : construct label array
    labels = dict((x,0) for x in edges.keys())
    
    # step 3 : region growing
    label = 1
    for x in labels : 
        if labels[x] == 0:
            stack = [x]
            # growing    
            while len(stack) > 0 :
                y = stack.pop()
                labels[y] = label
                for z in edges[y] : 
                    if labels[z] == 0 : stack.append(z)
            # next cluster    
            label = label + 1 
    
    # step 4 : find cluster size
    clusters = {}
    for k,v in labels.items() :
        if v not in clusters : clusters[v] = 1
        else :   clusters[v] = clusters[v] + 1
    num_unclustered_nodes = n - sum(clusters.values())
    
    # step 5 : calculate totol combo
    return calculate_total_combo(list(clusters.values()), num_unclustered_nodes)

