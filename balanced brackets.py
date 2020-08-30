def isBalanced(s):
    stack = []
    for c in list(s) :
        if   c == '(' : stack.append('(')
        elif c == '[' : stack.append('[')
        elif c == '{' : stack.append('{')
        elif c == ')' :
            if len(stack)==0 or stack[len(stack)-1] != '(' : return 'NO'
            else : stack.pop()
        elif c == ']' :
            if len(stack)==0 or stack[len(stack)-1] != '[' : return 'NO'
            else : stack.pop()
        elif c == '}' :
            if len(stack)==0 or stack[len(stack)-1] != '{' : return 'NO'
            else : stack.pop()
    return 'YES'

# Dont forget to check empty stack
# Stack is implemented with list
# Stack top is done by stack[len(stack)-1]
