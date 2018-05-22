import copy
def find_all(a,i,j,k,list,b,map):
    if len(b)>k:
        return list
    for z in range(j+1,len(a),1):
        map2=copy.copy(map)
        b2=copy.copy(b)
        if a[z] not in map:
            map2[a[z]]=1
            b2+=a[z]
            if len(b2)==k:
                list.append(b2)
            elif len(b2)<k:
                find_all(a,i,z,k,list,b2,map2)
    return list
def simpler_way(string,k):
    res=0
    n=len(string)
    for i in range(n):
        count=0
        cnt=[0]*26
        for j in range(i,n):
            if cnt[ord(string[j])-ord('a')]==0:
                count+=1
            cnt[ord(string[j])-ord('a')]+=1
            if count==k:
                res+=1
    return res


a="abc"
print(simpler_way(a,3))
# list1=[]
# for i in range(len(a)-2):
#     map={}
#     map[a[i]]=1
#     list=[]
#     b=a[i]
#     list1.extend(find_all(a,i,i,3,list,b,map))
# print(list1)


# simpler way


