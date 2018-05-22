def calllis(array):
    maxlength=0
    for i in range(len(array)):
        list=[]
        list=lis(array[i:len(array)],0,list)
        length=len(list)
        maxlength=max(length,maxlength)
    return maxlength

def lis(array,i,list):
    list.append(array[i])
    for j in range(i+1,len(array),1):
        if array[j]>array[i]:
            lis(array[j:len(array)],i,list)
            break
    return list

def overlap(a):
    lis=[1]*len(a)
    for i in range(1,len(a),1):
        for j in range(0,i,1):
            if a[j]<a[i] and lis[i]<lis[j]+1:
                lis[i]=lis[j]+1
    maximum=0
    for i in range(len(lis)):
        maximum=max(maximum,lis[i])
    return maximum

global maxi

def gfgsol(array,n):
    global maxi
    if n==1:
        return 1
    maxtillhere=1
    for i in range(1,n):
        res=gfgsol(array,i)
        if a[i-1]<a[n-1] and res+1>maxtillhere:
            maxtillhere=res+1
    maxi=max(maxi,maxtillhere)
    return maxtillhere



print(overlap([1,2,10,3,9,4,5,98,6,7]))
a=[1,2,10,3,9,4,5,98,6,7]
global maxi
maxi=1
print(gfgsol(a,len(a)))
# print(calllis([1,2,10,3,9,4,5,98,6,7]))