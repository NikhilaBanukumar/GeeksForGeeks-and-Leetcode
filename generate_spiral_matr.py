def generateMatrix(n):
    a=[[0 for x in range(n)] for y in range(n)]
    if n%2==0:
        max=n/2
    else:
        max=int(n/2)+1
    i=0
    k=1
    max_ring=n-1
    if max_ring==0:
        a[0][0]=1
    while i<max and max_ring>0:
        left=i
        right=i
        flag=0
        while left==i and right<max_ring:
            a[left][right]=k
            k+=1
            right+=1
            flag=1

        while right==max_ring and left<max_ring:
            a[left][right]=k
            k+=1
            left+=1

        while left==max_ring and right>i:
            a[left][right]=k
            k+=1
            right-=1

        while right==i and left>i:
            a[left][right]=k
            k+=1
            left-=1

        if left==i and right==i:
            if flag==0:
                a[left][right]=k
            i+=1
            max_ring-=1
    print(a)

generateMatrix(0)

