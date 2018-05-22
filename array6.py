def singletraversal(array):
    neg1=-1
    neg2=-1
    pos1=0
    pos2=0
    for i in range(len(array)):
        if array[i]>pos1:
            pos2 =pos1
            pos1=array[i]
        elif array[i]<=neg1:
            neg2 = neg1
            neg1=array[i]
    if pos1*pos2 > neg1*neg2:
        return [pos1,pos2]
    else:
        return [neg1,neg2]

print(singletraversal([-1, -3, -4,2,4, -5]))