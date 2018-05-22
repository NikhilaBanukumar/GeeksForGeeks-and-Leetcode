def delete_pallindrome_count(string):
    n=len(string)
    dp=[[0 for n in range(n)] for m in range(n)]
    for len1 in range(1,n,1):
        i=0
        for j in range(len1-1,n,1):
            if len1==1:
                dp[i][j]=1
            else:
                dp[i][j]=1+dp[i+1][j]
                if string[i]==string[i+1]:
                    dp[i][j]=min(1+dp[i+2][j],dp[i][j])
                for k in range(i+2,j+1,1):
                    if string[i]==string[k]:
                        dp[i][j]=min(dp[i+1][k-1]+dp[k+1][j],dp[i][j])
            i+=1
    return dp[0][n-1]


print(delete_pallindrome_count("2553432"))