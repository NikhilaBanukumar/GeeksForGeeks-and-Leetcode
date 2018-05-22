def pallindrome(strings,k,l):
    m=k
    for n in range(l,k,-1):
        if strings[m]!=strings[n]:
            return False
        m+=1
    return True


def find_pallindrome_substrings(strings,i,j):
    count=0
    for k in range(i,j+1,1):
        count+=1
        for l in range(j,k,-1):
            pallin=pallindrome(strings,k,l)
            if pallin:
                count+=1
    return count

def simpler(str):
    n=len(str)
    dp=[[0 for i in range(n)]for j in range(n)]
    ispalin=[[0 for i in range(n)] for j in range(n)]
    for i in range(n-1,-1,-1):
        dp[i][i]=1
        ispalin[i][i]=1
        for j in range(i+1,n,1):
            print(str[i]+"  "+str[j])
            ispalin[i][j]= (str[i]==str[j]) and ((i+1>j-1) or (1 if ispalin[i+1][j-1]!=0 else 0))
            dp[i][j]=dp[i][j-1]+dp[i+1][j]-dp[i+1][j-1]+ispalin[i][j]
    for i in ispalin:
        print(i)
    print("")
    for i in dp:
        print(i)
    print(dp[3][5])


# print(find_pallindrome_substrings("xyaabax",2,3))
simpler("xyaabaa")