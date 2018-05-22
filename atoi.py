def myAtoi(str):
    str2 = ""
    i = 0
    for i in range(len(str)):
        if str2!="" and not str[i].isdigit():
            break
        elif str2=="" and not str[i].isdigit() and str[i]!=" ":
            if str[i]=="+" and i<len(str)-1 and str[i+1].isdigit():
                continue
            elif str[i]=="-" and i<len(str)-1 and str[i+1].isdigit():
                continue
            else:
                return 0
        elif str[i].isdigit():
            if i>0 and str[i-1]=="-":
                if str[i]=="0":
                    str2+=str[i-1]
                else:
                    str2=str[i-1:i+1]
            elif str[i]=="0" and str2!="" and str2[len(str2)-1].isdigit():
                str2+=str[i]
            elif str[i]!=0:
                str2+=str[i]

    if str2=="" or str2=="-":
        return 0
    i=int(str2)
    if i<=-1*pow(2,31):
        return -1*pow(2,31)
    elif i>=pow(2,31):
        return pow(2,31)-1
    return i

# print(myAtoi("+-2"))
a="-       "
print(a.strip(),end="")
print("baby")