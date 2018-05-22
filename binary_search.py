def binary_search(a,l,r,key):
    print(a)
    print(l)
    print(r)
    if l<r:
        mid=int((l+(r-1))/2)
        if a[mid]==key:
            return mid
        elif a[mid]<key:
            return binary_search(a,mid+1,r,key)
        else:
            return binary_search(a,0,mid-1,key)
    else:
        return -1

a=[1,2,4,6,8,10]
n=len(a)
print(binary_search(a,0,n-1,5))
