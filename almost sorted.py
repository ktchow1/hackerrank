def almostSorted(arr):
    trend1_start = -1
    trend1_end   = -1
    trend2_start = -1
    trend2_end   = -1
    
    for n in range(len(arr)-1):
        # state 1
        if trend1_start < 0 :
            if arr[n+1] < arr[n] : trend1_start = n
        
        # state 2
        elif trend1_end < 0 :
            if arr[n+1] > arr[n] : trend1_end = n

        # state 3
        elif trend2_start < 0 :
            if arr[n+1] < arr[n] : 
                if trend1_end - trend1_start == 1 : trend2_start = n
                else :
                    print('no')
                    return None

        # state 4
        elif trend2_end < 0 :
            if arr[n+1] > arr[n] : 
                if n - trend2_start == 1 : trend2_end = n
                else :
                    print('no') # impossible case
                    return None
            else : 
                print('no') # trend2 cannot be longer than 1
                return None
        
        # state 5
        elif arr[n+1] < arr[n] :
            print('no')
            return None

    """
    print('trend1_start', trend1_start)
    print('trend1_end',   trend1_end)
    print('trend2_start', trend2_start)
    print('trend2_end',   trend2_end) """
    if trend1_start >= 0 and trend1_end < 0 : trend1_end = len(arr)-1
    if trend2_start >= 0 and trend2_end < 0 : trend2_end = len(arr)-1       

    # If there exists one trend ...
    if trend1_start < 0 and trend2_start < 0 : print('yes')             
    elif trend1_start >= 0 and trend2_start < 0 : 
        flag0 = (trend1_start == 0 or arr[trend1_end] >= arr[trend1_start-1])
        flag1 = (trend1_end == len(arr)-1 or arr[trend1_start] <= arr[trend1_end+1])
        if flag0 and flag1 :
            print('yes')             
            if arr[trend1_start+1] == arr[trend1_end] : 
                   print('swap', trend1_start+1, trend1_end+1) # index starts from 1 (instead of 0)
            else : print('reverse', trend1_start+1, trend1_end+1) 
        else : print('no') 

    # If there exists two trends, where both trends have size 1, then swap between trend1_start and trend2_end 
    elif trend1_start >= 0 and trend2_start >= 0 :
        flag0 = (arr[trend1_start] >= arr[trend2_start])
        flag1 = (arr[trend2_end]   <= arr[trend1_end])
        flag2 = (trend2_end == len(arr)-1 or arr[trend1_start] <= arr[trend2_end+1])
        flag3 = (trend1_start == 0 or arr[trend2_end] >= arr[trend1_start-1])

        if flag0 and flag1 and flag2 and flag3 : 
               print('yes') 
               print('swap', trend1_start+1, trend2_end+1) # index starts from 1 (instead of 0)
        else : print('no')
    else : print('no') # impossible case



    
