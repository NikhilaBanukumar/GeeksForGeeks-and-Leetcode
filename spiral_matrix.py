def spiral( a):
    main = []
    k=0
    l=0
    m= len(a)
    n= len(a[0])
    while k<m and l< n:
        for i in range(l,n):
            main.append(a[k][i])
        k+=1

        for i in range(k,m):
            main.append(a[i][n-1])
        n-=1

        if k<m:
            for i in range(n-1,l-1,-1):
                main.append(a[m-1][i])
            m-=1

        if l<n:
            for i in range(m-1,k-1,-1):
                main.append(a[i][l])
            l+=1

    return main

a=[[0 for i in range(3)] for j in range(5)]
a[0][0]=2
a[0][1]=3
a[0][2]=4
a[1][0]=5
a[1][1]=6
a[1][2]=7
a[2][0]=8
a[2][1]=9
a[2][2]=10
a[3][0]=11
a[3][1]=12
a[3][2]=13
a[4][0]=14
a[4][1]=15
a[4][2]=16
print(spiral(a))


