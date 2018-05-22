def valid_parenthesis(str):
    map={"[":"]","(":")","{":"}"}
    stack=[]
    for i in range(len(str)):
        if stack==[]:
            if str[i] not in map:
                return False
            stack.append(str[i])
        elif map[stack[len(stack)-1]]==str[i]:
            stack.pop()
        else:
            if str[i] not in map:
                return False
            stack.append(str[i])
    print(stack)
    if stack==[]:
        return True
    else:
        return False


print(valid_parenthesis(")["))