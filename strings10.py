def anagram_substrings(string,i,j,n):
    if j<=n:
        return 0
    if i==j:
        return 0
    if string[i]==string[j]:
        return 1+anagram_substrings(string,i+1,j-1,n)
    else:
        if i==n:
            return anagram_substrings(string,i,j-1,n)
        else:
            return 0

a="xyyzyxz"
count1=0
map={}
for i in range(len(a)-1):
    if a[i] not in map:
        map[a[i]]=1
        count1+=anagram_substrings(a,i,len(a)-1,i)
print(count1)