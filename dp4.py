import sys

def mincost(matrix,n,m):
    if m<0 or n<0:
        return sys.maxsize
    if m==0 and n==0:
        return matrix[n][m]
    else:
        return matrix[n][m]+min(mincost(matrix,n-1,m-1),mincost(matrix,n,m-1),mincost(matrix,n-1,m))

def overlap(matrix,n,m):
    a=[[0 for i in range(n)]for j in range(m)]
    for i in range(n):
        a[i][-1]=sys.maxsize
    for j in range(m):
        a[-1][j]=sys.maxsize
    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                a[i][j]=matrix[i][j]
            else:
                a[i][j]=matrix[i][j]+min(a[i-1][j-1],a[i-1][j],a[i][j-1])
    return a[n-1][m-1]

n=3
m=3
matrix=[[0 for i in range(n)]for j in range(m)]
matrix[0][0]=1
matrix[0][1]=2
matrix[0][2]=3
matrix[1][0]=4
matrix[1][1]=8
matrix[1][2]=2
matrix[2][0]=1
matrix[2][1]=5
matrix[2][2]=3
print(mincost(matrix,n-1,m-1))
print(overlap(matrix,n,m))