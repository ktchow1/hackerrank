"""
Given list-of-list A, where A[ny][nx] is height of square-prism at (ny,nx).
Suppose the base of each prism is 1x1, find the total surface area.
Beware of concave cases, besides don't forget the top and bottom.
"""

def wall_area_for_line(x) :
    area = x[0] + x[len(x)-1]
    for n in range(len(x)-1) : area = area + abs(x[n]-x[n+1])
    return area

def surfaceArea(A):
    sz_y = len(A)
    sz_x = len(A[0])
    area = sz_y * sz_x * 2
    for n in range(sz_y) : area = area + wall_area_for_line(A[n])
    for n in range(sz_x) : area = area + wall_area_for_line([row[n] for row in A])
    return area
