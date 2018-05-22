def mySqrt(x):
    if x==0:
        return (0,0,0)
    a=mySqrt(int(x/100))
    divisor=a[0]
    quotient=a[1]
    remainder=a[2]
    curr=(remainder*100)+(x%100)
    max=0
    for i in range(0,10):
        sqr=(divisor*10+i)*(i)
        if sqr<=curr:
            max=divisor*10+i
            remainder=curr-sqr
        else:
            break
    if sqr== curr or max%10==9:
        quotient = quotient * 10 +(i)
        divisor=max+i
    else:
        quotient=quotient*10+(i-1)
        divisor=max+(i-1)
    return (divisor,quotient,remainder)


a=mySqrt(1978959248)
print(a[1])