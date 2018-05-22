def countsubstring(string,i,k):
    array=[0]*26
    array[ord(string[i])-ord("a")]=1
    for j in range(i+1,len(string)):
        if array[ord(string[j])-ord("a")]==0:
            sum=0
            for i in array:
                sum+=i
            if sum<k:
                array[ord(string[j]) - ord("a")] =1
            else:
                return (j-i)
    sum=0
    for i in array:
        sum+=i
    if sum==k:
        return (j-i)+1
    else:
        return -1


def find_max_substring(string,k):
    count=0
    str=""
    for i in range(len(string)):
        countret=countsubstring(string,i,k)
        if countret>count:
            count=countret
            str=string[i:count+i]
    print(str)

find_max_substring("abacddde",3)
