def reverse(num):
    a=bin(num)
    a=a[2:]
    n=32-len(a)
    c=""
    for i in range(n):
        c+="0"
    a=c+a
    print(int(a[::-1],2))
reverse(43261596)