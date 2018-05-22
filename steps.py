def recursion(n):
    res=[0 for x in range(n+1)]
    res[0],res[1]=1,1
    for i in range(2,n):
        j=1
        while j<=2 and j<=i:
            res[i]=res[i]+res[i-j]
            j+=1
    return res[n-1]

print(recursion(4+1))