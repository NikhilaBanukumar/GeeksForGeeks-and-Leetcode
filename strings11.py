def countchange(str1,str2,k):
    if len(str1)!=len(str2):
        return True
    st1=[0]*26
    st2=[0]*26
    for i in range(len(str1)):
        st1[ord(str1[i])-ord("a")]+=1
    for i in range(len(str2)):
        st2[ord(str2[i])-ord("a")]+=1
    count=0
    for i in range(26):
        if st1[i]>st2[i]:
            count+=abs(st1[i]-st2[i])
    if count<=k:
        return "Yes"
    else:
        return "No"

print(countchange("geeks","eggkf",1))