def merge(nums1, m, nums2, n):
    j = 0
    for i in range(m, len(nums1)):
        nums1[i] = nums2[j]
        j += 1
    print(nums1)
    nums1.sort()
    return

merge([1,2],0,[2,5,6],3)