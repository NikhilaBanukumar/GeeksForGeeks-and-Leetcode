def threeSum(nums):
    dic = {}
    for num in nums:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
    if 0 in dic and dic[0] >= 3:
        ans = [[0, 0, 0]]
    else:
        ans = []
    ns = sorted([x for x in dic if x < 0], reverse=True)
    print(ns)
    nns = sorted([x for x in dic if x >= 0])
    print(nns)
    for i in ns:
        for j in nns:
            chk = -(j + i)
            if chk in dic:
                if chk in [i, j] and dic[chk] > 1:
                    ans.append([i, chk, j])
                elif chk < i:
                    ans.append([chk, i, j])
                elif j < chk:
                    ans.append([i, j, chk])
    return ans

print(threeSum([-1,0,1,-1,2,-4]))