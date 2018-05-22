def reverse_string_using_stack(string):
    stack=[]
    for i in range(len(string)):
        stack.append(string[i])
    string=""
    for i in range(len(stack)):
        string+=stack.pop()
    print(string)

string="ABCDEF"
reverse_string_using_stack(string)