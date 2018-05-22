def merge(arr,l,m,r):
    print("l:" + str(l) + "m:" + str(m) + "r:" + str(r))
    n1=m-l+1
    n2=r-m
    L=[0]*(n1)
    R=[0]*(n2)

    for i in range(0,n1):
        L[i]=arr[l+i]
        print("L:"+str(L[i]))
    for j in range(0,n2):
        R[j]=arr[m+j+1]
        print("R:"+str(R[j]))

    i = 0
    j = 0
    k = l

    while i<n1 and j<n2:
        if L[i]<=R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1

    while i<n1:
        arr[k]=L[i]
        i+=1
        k+=1

    while j<n2:
        arr[k]=R[j]
        j+=1
        k+=1
    c = ""
    for i in range(n):
        c += str(arr[i]) + " "

    print(c)


def mergesort(arr,l,r):
    if l<r:

        m=int(((l+r)/2))
        # print("l:" + str(l) + "m:" + str(m)+"r:"+str(r))
        mergesort(arr,l,m)
        mergesort(arr,m+1,r)
        merge(arr,l,m,r)


arr=[5,4,10,1,6,3,8]
n=len(arr)
mergesort(arr,0,n-1)
c=""
for i in range(n):
    c+=str(arr[i])+" "

print(c)




