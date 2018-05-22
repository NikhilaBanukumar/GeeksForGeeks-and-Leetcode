def reverse(string):
    i=0
    j=len(string)-1
    temp=toList(string)
    while i<j:
        if string[i].isalpha()==0:
            i+=1
        elif string[j].isalpha()==0:
            j-=1
        if string[i].isalpha()==1 and string[j].isalpha()==1:
            temp[i],temp[j]=temp[j],temp[i]
            i+=1
            j-=1
    temp="".join(temp)
    return temp

def toList(string):
    list=[]
    for i in range(len(string)):
        list.append(string[i])
    return list

print(reverse("a!!!b.c.d,e'f,ghi"))