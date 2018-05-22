def count(array,m,n):
    if n==0:
        return 1
    #array=[1,5,10,25] m=3 n=100
    if n<=0:
        return 0
    if m<=0 and n>=1:
        return 0
    return count(array,m-1,n)+count(array,m,n-array[m-1])

print(count([1,5,10,25],4,5))