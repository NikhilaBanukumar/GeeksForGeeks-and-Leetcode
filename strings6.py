def palindrome(string,i,j):
    if i==j:
        return True
    if string[i]==string[j]:
        return palindrome(string,i+1,j-1)
    return False

a="malayalam"
print(palindrome(a,0,len(a)-1))