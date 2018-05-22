def commonletters(str1,str2):
    str1map=[0]*26
    str2map=[0]*26
    a=""
    for i in range(len(str1)):
        str1map[ord(str1[i])-ord("a")]+=1
    for i in range(len(str2)):
        str2map[ord(str2[i])-ord("a")]+=1
    for i in range(26):
        if str1map[i]!=0 and str2map[i]!=0:
            minimum=min(str1map[i],str2map[i])
            for j in range(minimum):
                a+=chr(ord("a")+i)
    return a

print(commonletters("hhhhhhello","gfghhmh"))