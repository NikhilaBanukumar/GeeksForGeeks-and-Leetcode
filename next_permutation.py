def nextPermutation(nums):
    n=len(nums)
    if n==0 or n==1:
        return n
    i=n-2
    for i in range(n-2,-1,-1):
        if nums[i]<=nums[i+1]:
            i_pos=i
            break
    j=n-1
    for j in range(n-1,i_pos,-1):
        if nums[j]>=nums[i_pos]:
            j_pos=j
            break

    while i<=j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j=n-1
        while i<j and nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums

print(nextPermutation([3,2,1]))