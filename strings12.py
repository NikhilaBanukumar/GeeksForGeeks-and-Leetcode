def palindrome_stream(string):
    n=len(string)
    print(string[0]+"yes")
    if n==1:
        return
    firststr=ord(string[0])%103
    secondstr=ord(string[1])%103
    h=1
    i=0
    j=0
    for i in range(1,n):
        if firststr==secondstr:
            for j in range(0,int(i/2)):
                if string[j]!=string[j-1]:
                    break
            j+=1
            if j==int(i/2):
                print(string[i]+"yes")
            else:
                print(string[i]+"No")
        else:
            print(string[i]+"No")
        if i!=(n-1):
            if i%2==0:
                h=(h*256)%103
                firststr=(firststr+(h*ord(string[int(i/2)])))%103
                secondstr=((secondstr*256)+ord(string[int(i+1)]))%103
            else:
                secondstr=((256*((secondstr+103)-ord(string[int((i+1)/2)])*h)%103)+ord(string[i+1]))%103

def palindrome(string):
    i=0
    for j in range(len(string)):
        if i==j:
            print(string[j]+"Yes")
        elif string[i]!=string[j]:
            print(string[j]+"No")
        elif string[i]==string[j]:
            for k in range(j,int(j/2),-1):
                if string[i+1]!=string[k-1]:
                    print(string[j]+"No")
                    break
                i+=1
            i=0
            if (k-1)<=int(j/2):
                print(string[j]+"yes")

# palindrome_stream("aabaacaabaa")
palindrome("abcba")

