def uniquePaths(m, n):
    array = [[0 for x in range(m)] for y in range(n)]
    for i in range(m):
        array[n - 1][i] = 1
    for i in range(n):
        array[i][m-1]=1
    print(array)
    i=n-2
    while i>=0:
        j=m-2
        while j>=0:
            array[i][j]=array[i+1][j]+array[i][j+1]
            j-=1
        i-=1
    print(array[0][0])
uniquePaths(2,2)
