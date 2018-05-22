def count(string):
    map={}
    for i in range(len(string)):
        if string[i] not in map:
            map[string[i]]=1
        else:
            map[string[i]]+=1
    min=len(string)
    max=0
    for i in map:
        if map[i]<min:
            min=map[i]
        if map[i]>max:
            max=map[i]
    if max-min==1:
        return True
    else:
        return False

print(count("xxxxxyzzz"))