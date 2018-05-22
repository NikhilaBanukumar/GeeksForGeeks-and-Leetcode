def rotate(array):
    j=len(array)-1
    i=0
    while i<j:
        left=i
        right=i
        while right<j:
            temp=array[right][j]
            array[right][j]=array[left][right]
            temp1=array[j][len(array)-right-1]
            array[j][len(array)-right-1]=temp
            temp=array[len(array)-right-1][i]
            array[len(array)-right-1][i]=temp1
            array[left][right]=temp
            right+=1
        j-=1
        i+=1
    return

array=[[0 for i in range(4)] for j in range(4)]
array[0][0]=1
array[0][1]=2
array[0][2]=3
array[0][3]=4
array[1][0]=5
array[1][1]=6
array[1][2]=7
array[1][3]=8
array[2][0]=9
array[2][1]=10
array[2][2]=11
array[2][3]=12
array[3][0]=13
array[3][1]=14
array[3][2]=15
array[3][3]=16
rotate(array)
print(array)