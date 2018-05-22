def hammingWeight(n):
    a = bin(n)
    a = int(a[2:])
    count = 0
    while a > 0:
        d = a % 10
        if d == 1:
            count += 1
        a = int(a / 10)
    print(count)

hammingWeight(11)