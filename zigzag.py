def printzigzag(string,rows):
    if rows==1 or rows>len(string):
        return string
    diff=rows-2
    n=len(string)
    temp=""
    for i in range(rows):
        if i==0 or i==rows-1:
            j=i
            while j<=n-1:
                temp+=string[j]
                j+=rows+diff
        else:
            temp+=string[i]
            below=(rows+diff)-(2*i)
            top=(rows+diff)-below
            pos=i
            while pos<=n-1:
                if pos+below<=n-1:
                    temp+=string[pos+below]
                    pos=pos+below
                    if pos+top<=n-1:
                        temp+=string[pos+top]
                        pos=pos+top
                    else:
                        break
                else:
                    break
    return temp


print(printzigzag("a",3))

