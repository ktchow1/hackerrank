# Given a string w of alphabets, find the next word right after w in dictionary.

def biggerIsGreater(w):

    for n in range(len(w)-1,0,-1) :
        if w[n-1] < w[n] : break
    else : return 'no answer'
    
    x = min([c for c in w[n:] if c > w[n-1]])    
    y = w[n-1:].replace(x,'',1) # erase first encountered x (DONT replace more than once)
    z = ''.join(sorted(y))
    return w[:n-1] + x + z 
