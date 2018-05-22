def number_reverse(number):
    if number < (-1 * pow(2, 31)) or number > (pow(2, 31) - 1):
        return 0
    x=number
    count=0
    while x!=0:
        x=int(x/10)
        count+=1
    x=abs(number)
    cur=0
    while count!=0:
        cur+=(x%10)*(pow(10,count-1))
        x=int(x/10)
        count-=1
    if abs(number)==number:
        return cur
    else:
        return -1*cur

a="a"
print(a.isal)

# print(number_reverse(9646324351))
