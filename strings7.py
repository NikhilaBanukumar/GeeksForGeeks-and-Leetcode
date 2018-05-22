def printrest(string,char,n):
    count=0
    for i in range(len(string)):
        if string[i]==char:
            count+=1
            if count==n:
                return string[i+1:]
    return "No string remaining"

print(printrest("this is a demo string","i",5))