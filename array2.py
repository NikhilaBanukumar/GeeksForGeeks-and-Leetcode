import sys

def getpair(arr1,arr2,number):
    max=0
    for i in range(len(arr1)):
        if number>arr1[i] and arr1[i]>max:
            max=arr1[i]
    for j in range(len(arr2)):
        if number>arr2[j] and arr2[j]>max:
            max=arr2[j]
    number=number-max
    min=0
    for i in range(len(arr1)):
        if number>arr1[i] and arr1[i]>min:
            min=arr1[i]
    for j in range(len(arr2)):
        if number>arr2[j] and arr2[j]>min:
            min=arr2[j]
    return [min,max]

def simpler(arr1,arr2,number):
    max=sys.maxsize
    l=0
    r=len(arr2)-1
    while l<len(arr1)-1 and r>=0:
        if abs((arr1[l]+arr2[r])-number)<max:
            left=arr1[l]
            right=arr2[r]
            max=abs((arr1[l]+arr2[r])-number)

        if arr1[l]+arr2[r]>number:
            r=r-1
        else:
            l=l+1

    print(str(left)+str(right))

arr1=[1,4,5,7]
arr2=[10,20,30,40,50]
number=56
print(getpair(arr1,arr2,number))
simpler(arr1,arr2,number)