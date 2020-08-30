
class pair : pass

def next_entry(point_orig, offset, opsize) :
    # deep copy of point is necessary
    point = pair()
    point.y = point_orig.y
    point.x = point_orig.x

    if point.y == offset.y :
        if point.x < offset.x + opsize.x - 1 : point.x = point.x+1
        else : point.y = point.y+1
    elif point.x == offset.x + opsize.x -1 :
        if point.y < offset.y + opsize.y - 1 : point.y = point.y+1
        else : point.x = point.x-1
    elif point.y == offset.y + opsize.y -1 :
        if point.x > offset.x : point.x = point.x-1
        else : point.y = point.y-1
    elif point.x == offset.x :
        if point.y > offset.y : point.y = point.y-1
        else : point.x = point.x+1
    else : print('incorrect tracking')
    return point

def rotate(mat_src, offset, opsize, r) :
    # deep copy of matrix is necessary
    mat_dst = [row.copy() for row in mat_src]     
    
    num_boundary = (opsize.y + opsize.x - 2) * 2
    net_rotation = r % num_boundary
    dst = pair() # dst-coord
    src = pair() # src-coord
    dst.y, dst.x = offset.y, offset.x
    src.y, src.x = offset.y, offset.x
    for n in range(net_rotation) : src = next_entry(src, offset, opsize)
    for n in range(num_boundary) :
        mat_dst[dst.y][dst.x] = mat_src[src.y][src.x]
        dst = next_entry(dst, offset, opsize)
        src = next_entry(src, offset, opsize)
        
    return mat_dst

def matrixRotation(matrix, r):
    offset = pair()    
    opsize = pair()
    offset.y = 0
    offset.x = 0    
    opsize.y = len(matrix)
    opsize.x = len(matrix[0])
    
    while opsize.y > 0 and opsize.x > 0 :
        matrix = rotate(matrix, offset, opsize, r)
        offset.y = offset.y + 1
        offset.x = offset.x + 1
        opsize.y = opsize.y - 2
        opsize.x = opsize.x - 2
    
    for row in matrix :        
        for x in row : print(x, end = ' ')
        print(' ')

    
initpt = pair
iterpt = pair
offset = pair()
opsize = pair()
initpt.y = 0
initpt.x = 0
offset.y = 0
offset.x = 0
opsize.y = 6
opsize.x = 7

iterpt.y = initpt.y
iterpt.x = initpt.x
while True :
    print(iterpt.y, iterpt.x)
    iterpt = next_entry(iterpt, offset, opsize)
    if iterpt.y == initpt.y and iterpt.x == initpt.x : break
    
        
        
