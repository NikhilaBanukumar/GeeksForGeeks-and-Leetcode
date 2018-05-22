def rotate(nums, k):
    n=len(nums)
    if k>n:
        k=k%n
    k=n-k
    gc=gcd(k,n)
    for i in range(gc):
        j=i
        temp=nums[i]
        while 1:
            d=j+k
            if d>=n:
                d=d-n
            if d==i:
                break
            nums[j]=nums[d]
            j=d
        nums[j]=temp
    print(nums)

def gcd(k,n):
    if n==0:
        return k
    else:
        return gcd(n,k%n)

nums=[1,2,3,4,5,6]
k=2
rotate(nums,k)
