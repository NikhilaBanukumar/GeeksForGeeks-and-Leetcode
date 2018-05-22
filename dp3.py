def editdistance(str1,str2,m,n):
    if m==0:
        return n
    if n==0:
        return n
    if str1[m-1]==str2[n-1]:
        return editdistance(str1,str2,m-1,n-1)

    else:
        return 1+min(editdistance(str1,str2,m-1,n),editdistance(str1,str2,m,n-1),editdistance(str1,str2,m-1,n-1))

def memo(str1,str2,m,n):
    dp=[[0 for i in range(n+1)] for j in range(m+1)]
    for i  in range(m+1):
        for j in range(n+1):
            if j==0:
                dp[i][j]=i
            elif i==0:
                dp[i][j]=j
            if str1[i-1]==str2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
    return dp[m][n]





str1="geek"
str2="geek"
print(editdistance(str1,str2,len(str1),len(str2)))
print(memo(str1,str2,len(str1),len(str2)))