def threeSumClosest(nums, target):
    dict = {}
    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    n = sorted([x for x in dict if x < 0], reverse=True)
    p = sorted([x for x in dict if x >= 0])


