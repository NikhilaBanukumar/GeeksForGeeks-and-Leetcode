def c(str1,str2,i,j,a):
    if i>=len(str1) or j>=len(str2):
        return a

    if str1[i]==str2[j]:
        a+=str1[i]
        return c(str1,str2,i+1,j+1,a)
    else:
        cmb1=c(str1,str2,i+1,j,a)
        cmb2=c(str1,str2,i,j+1,a)
        if len(cmb1)>len(cmb2):
            return cmb1
        else:
            return cmb2

print(c("AGGTAB","GXTXAYB",0,0,''))

