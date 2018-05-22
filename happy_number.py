def isHappy(n):
    set = []
    count=1
    while n > 1 and count<50:
        set.append(n)
        sum = 0
        num = n
        while num != 0:
            nums = num % 10
            sum += nums ** 2
            num = int(num / 10)
        n = sum
        count+=1
    print(set)
    if n == 1:
        return True
    else:
        return False
isHappy(4)