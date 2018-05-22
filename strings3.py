def final(string,k):
    map={}
    for i in range(len(string)):
        if string[i] not in map:
            map[string[i]]=1
        else:
            map[string[i]]+=1
    a=""
    for j in range(len(string)):
        if map[string[j]]==1:
            a+=string[j]

    for i in range(len(a)):
        if i==(k-1):
            return a[i]
    return "Wrong value for k"
def simpler_way(string,k):
    maxchar=256
    count=[0]*maxchar
    index=[0]*maxchar
    n=len(string)
    for i in range(maxchar):
        count[i]=0
        index[i]=n
    for j in range(n):
        count[ord(string[j])]+=1
        if count[ord(string[j])]==1:
            index[ord(string[j])]=j
        else:
            index[ord(string[j])]=n
    array=sorted(index)
    return string[array[k-1]]


print(final("geeksforgeeks",3))
print(simpler_way("geeksforgeeks",1))