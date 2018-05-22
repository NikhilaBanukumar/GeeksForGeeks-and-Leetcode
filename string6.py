def substrings(string):
    count = 0
    for i in range(len(string)):
        for j in range(i,len(string)):
            if string[j]==string[i]:
                count+=1
    return count

def other_method(string):
    result=0
    n=len(string)
    count=[0]*26
    for i in range(n-1):
        print("i:"+str(i))
        print(ord(string[i])-ord("a"))
        count[ord(string[i])-ord("a")]+=1
    print(count)
    for i in range(26):
        result+=count[i]*(count[i]+1)/2
    return int(result)

# string="abcab"
# print(ord(string[2])-ord("a"))
print(other_method("abcaba'"))
# print(substrings("abcab"))

