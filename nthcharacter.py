def nthchar(string,j,R):
    if j==(R):
        return string
    str=""
    for i in range(len(string)):
        if string[i]=="1":
            str+="10"
        elif string[i]=="0":
            str+="01"
    return nthchar(str,j+1,R)

def nthcharacter(string,R,N):
    if R==0:
        return(string[N])
    if ((int(len(string)/2))*(pow(2,R)))< N:
        str=""
        for j in range(int(len(string)/2),len(string)):
            if string[j] == "1":
                str += "10"
            elif string[j] == "0":
                str += "01"
        n=N%pow(2,R)
        return nthcharacter(str,R-1,n)
    else:
        str=""
        for j in range(int(len(string)/2)):
            if string[j] == "1":
                str += "10"
            elif string[j] == "0":
                str += "01"
        return nthcharacter(str,R-1,N)

R=20
N=3
n=3
# str1=nthchar("1000",0,20)
str2=nthcharacter("1000",R,N)
print(str2)
# for i in range(len(str1)):
#     if i ==n:
#         print(str1[n])
