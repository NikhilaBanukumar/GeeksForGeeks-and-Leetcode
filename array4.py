def crossingpoint(array,l,m,h):
    sm=0
    left_sum=-10000
    for i in range(m,l-1,-1):
        sm=sm+array[i]
        if sm>left_sum:
            left_sum=sm
    sm=0
    right_sum=-10000
    for i in range(m+1,h+1):
        sm=sm+array[i]
        if sm>right_sum:
            right_sum=sm
    return left_sum+right_sum

def findmaxsum(array,l,h):
    if l==h:
        return array[l]
    m= int((l+h)/2)
    return max(findmaxsum(array,l,m),findmaxsum(array,m+1,h),crossingpoint(array,l,m,h))

array=[-2,5,6,-2,-3,1,5,-6]
n=len(array)
max_sum=findmaxsum(array,0,n-1)
print(max_sum)