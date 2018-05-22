def push(stack,number):
    stack.append(number)

def pop(stack):
    a=stack.pop()
    return a

def isempty(stack):
    if len(stack)==0:
        return True
    else:
        return False
def top(stack):
    return stack[len(stack)-1]

def sortstack(stack,a):
    if isempty(stack):
        push(stack,a)
        return stack
    if top(stack)>a:
        temp=pop(stack)
        stack=sortstack(stack,a)
        push(stack,temp)
        return stack
    else:
        push(stack,a)
        return stack

def sort_stack_recursion(stack):
    if isempty(stack):
        return stack
    a=pop(stack)
    stack=sort_stack_recursion(stack)
    if isempty(stack):
        push(stack,a)
    elif top(stack)>a:
        stack=sortstack(stack,a)
    else:
        stack.append(a)
    return stack

stack=[30,-5,18,14,-3]
sort_stack_recursion(stack)
print(stack)
