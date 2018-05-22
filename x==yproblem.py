def xtoy(str1,str2,i,j):
    if j>=len(str2) and i<len(str1):
        return False
    if i==len(str1) and j>i:
        return True
    if str1[i]==str2[j] or str1[i]==str2[j].upper():
        return True and xtoy(str1,str2,i+1,j+1)
    else:
        return xtoy(str1,str2,i,j+1)


print(xtoy("ABcd","BCD",0,0))
