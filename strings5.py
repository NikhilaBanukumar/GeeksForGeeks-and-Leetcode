vowels=["a","e","i","o","u"]

def iteravtive(string):
    count=0
    for i in range(len(string)):
        if string[i].lower() in vowels:
            count+=1
    return count
def recursion(string,i):
    if i==1:
        a=string[i-1].lower() in vowels
        return a
    return (string[i-1].lower() in vowels)+recursion(string,i-1)
    # if i>=len(string):
    #     return 0
    # if i<len(string):
    #     if string[i].lower() in vowels:
    #         count=1+recursion(string,i+1)
    #     else:
    #         count=recursion(string,i+1)
    # return count



print(iteravtive("nikhila"))
print(recursion("nikhilaba",len("nikhilaba")))
