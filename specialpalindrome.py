def special_pallindrome(a,i,j,b):
    for n in range(j,i-1,-1):
        if b == n:
            return 0
        if i == n:
            return 1
        if i==b:
            if a[i]==a[n]:
                return special_pallindrome(a,i+1,n-1,b)
        else:
            if a[i]==a[n] and a[i]==a[i-1]:
                return special_pallindrome(a,i+1,n-1,b)
            if a[i]!=a[n] :
                return ((n-i)+1)*special_pallindrome(a,i,i,b)
                break
    return 0


a="bucubb"
maxi=0
# print(special_pallindrome(a,0,len(a)-1))
for i in range(len(a)):
    maxi+=special_pallindrome(a,i,len(a)-1,i)
print(maxi)
