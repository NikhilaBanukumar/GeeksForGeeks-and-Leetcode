import math
def getPermutation(n, k):
    a=math.factorial(n)
    if k >math.factorial(n):
        k=k%n
    a=[]
    for i in range(1,n+1):
        a.append(i)
    if k==1:
        return a
    b=0
    while b<(k-1):
        i = n - 1
        while i>0:
            if a[i-1]<a[i]:
                j=n-1
                while a[i-1]>a[j]:
                    j-=1
                a[i-1],a[j]=a[j],a[i-1]
                a[i:]=sorted(a[i:])
                b += 1
                break
            else:
                i-=1
    print("".join(str(x) for x in a))
getPermutation(9,331987)
a=[1,2,3,4]
a.remove()