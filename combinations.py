def combinationSum(c, target):
    main = []
    for i in range(len(c)):
        a = [c[i]]
        tar = target - c[i]
        findrest(tar,c[i:],a, main)
    print(main)


def findrest(tar, c, a, main):
    if tar == 0:
        b=list(a)
        b.sort()
        if b not in main:
            main.append(b)
        return
    if tar<0:
        return
    for i in c:
        if tar - i >=0:
            a.append(i)
            findrest(tar-i,c,a,main)
            a.pop()
    return


combinationSum([1,2,3,5,7,8],8)
