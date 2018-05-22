def myPow(x, n):
    if n < 0:
        x = 1 / x
    res=1
    n=abs(n)
    while n>0:
        pow = x
        cnt = 1
        while cnt+cnt <= n:
            pow = pow * pow
            cnt = cnt + cnt
        n=n-cnt
        res=res*pow
    if n%2==1:
        res=res*x
    return res

print(myPow(0.00001,2147483647))