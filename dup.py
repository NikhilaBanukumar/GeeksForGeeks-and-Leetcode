def permuteUnique(nums):
    ans = []
    traversal(nums, 0,ans)
    return ans


def traversal(nums, idx,ans):
    l = len(nums)
    if idx == l - 1:
        ans.append(nums.copy())
        return

    i = idx
    s = set()
    while i < len(nums):
        if nums[i] not in s:
            s.add(nums[i])
            nums[idx], nums[i] = nums[i], nums[idx]
            # print('swap: ', nums)
            traversal(nums, idx + 1,ans)
            nums[idx], nums[i] = nums[i], nums[idx]
        i += 1

print(permuteUnique([1,1,2]))