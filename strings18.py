import sys
def similiarity(word,str,i,j):
    if i>=len(word) or j>=len(str):
        return 0
    if word[i]==str[j]:
        return 1+similiarity(word,str,i+1,j+1)
    else:
        return max(similiarity(word,str,i,j+1),similiarity(word,str,i,j+1))

flag=0
def countdiff(word,str):
    i=0
    j=0
    flag=0
    count=0
    while i<len(word) and j<len(str):
        if word[i]==str[j]:
            if word[i:i+2] in str:
                i+=1
                j+=1
            else:
                flag=1
                i+=1
                j+=1
        elif word[i] in str[j:len(str)-1]:
            if flag==1:
                count+=1
            j+=1
        elif word[i] not in str[j:len(str)-1]:
            i+=1
    return count


def find_largest_string(dict,stri):
    maxmatch=0
    maxcount=sys.maxsize
    string=""
    for i in dict:
        similiar=similiarity(i,stri,0,0)
        diff=countdiff(i,stri)
        print(str(similiar)+":"+str(diff))
        if diff<maxcount or maxmatch<similiar:
                maxmatch=similiar
                maxcount=diff
                string=i
    print(string)


find_largest_string(["ale", "apple", "monkey", "plea"],"abpcplea" )

