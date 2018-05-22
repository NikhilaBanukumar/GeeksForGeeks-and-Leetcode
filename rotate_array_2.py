def rotate( nums, k):
    n = len(nums)
    if n==0:
        return
    if k >= n:
        k = k % n
    gc = gcd(k, n)
    for i in range(gc):
        temp = nums[i]
        j = i + k
        while j != i:
            temp2 = nums[j]
            nums[j] = temp
            temp = temp2
            j = j + k
            if j >=len(nums):
                j = j % (len(nums))
        if j==i:
            nums[i]=temp
    print(nums)

def gcd(k,n):
    if n==0:
        return k
    else:
        return gcd(n,k%n)

nums=[1,2,3,4,5,6,7]
rotate(nums,3)
print(nums)