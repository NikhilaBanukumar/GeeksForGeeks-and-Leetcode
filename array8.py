def printallsum_pairs(array,sum):
    list=[]
    i=0
    j=len(array)-1
    while i<j:
        if array[i]+array[j]==sum:
           a=[]
           a.append(array[i])
           a.append(array[j])
           list.append(a)
           i+=1
           j-=1
        elif array[j]+array[i]!=sum and sum-array[i]>array[j]:
            i+=1
        elif array[j]+array[i]!=sum and sum-array[i]<array[j]:
            j-=1
    print(list)

printallsum_pairs([-2,2,3,5,5,8,10,12],10)
