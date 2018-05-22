def start1end1(number):
    j=0
    sum=0
    for i in range(len(number)):
        if number[i]=="1":
            j+=1
            if j>1:
                sum+=(j-1)
    print(sum)

def without_duplicates(number):
    list=[]
    for i in range(len(number)):
        a=number[i]
        for j in range(i+1,len(number)):
            a+=number[j]
            list.append(a)
    map={}
    for str in list:
        if str[0]=="1" and str[len(str)-1]=="1":
            if str not in map:
                map[str]=1
    print(len(map))
# start1end1("100101")
without_duplicates("100101")