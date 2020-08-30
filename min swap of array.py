# Given contiguous unordered integers from 1 to N
# find min num of swaps to make it ordered.

"""
index array    count 
0     5241376  0
0     3241576  1
0     4231576  2
0     1234576  3
1     1234576  3
2     1234576  3
3     1234576  3
4     1234576  3
5     1234567  4
6     1234567  4
"""

def minimumSwaps(arr):
    index = 0
    count = 0
    while index < len(arr)-1 :
        if arr[index] == index+1 : index = index + 1
        else :
            # Please cache the index, otherwise it is error-prone.
            index_ = arr[index]-1
            arr[index], arr[index_] = arr[index_], arr[index]
            count = count + 1
    return count

""" C++
int minimumSwaps(vector<int> arr) 
{
    int count = 0;
    int index = 0;
    while(index!=arr.size()-1)
    {
        if (arr[index] != index+1)
        {
            std::swap(arr[index], arr[arr[index]-1]);
            ++count;
        }
        else ++index;
    }
    return count;
}
"""
