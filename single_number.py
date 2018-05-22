def single_number(array):
    prev=0
    for i in array:
        number=1<<i
        prev=prev^number
    count=0
    while prev%10!=0:
        prev=prev>>1
        count+=1
    if count==0:
        return count
    else:
        return count-1

print(single_number([1,1,6,6,6]))