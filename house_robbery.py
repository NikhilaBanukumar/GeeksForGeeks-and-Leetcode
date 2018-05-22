def rob(nums):
    n = len(nums)
    if n==0:
        return 0
    if n==1:
        return nums[0]
    if n==2:
        return max(nums[0],nums[1])
    diff = 1
    maxi = 0
    while diff + 1 < n:
        for i in range(diff+1):
            sum = nums[i]
            while i + diff + 1 < n:
                sum += nums[i + diff + 1]
                i = i + diff + 1
            if sum > maxi:
                maxi = sum
        diff+=1
    return maxi
print(rob([1,2]))