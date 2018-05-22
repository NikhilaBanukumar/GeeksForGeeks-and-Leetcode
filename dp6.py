import sys
def matrixmultiplication(array,i,j):
    if i==j:
        return 0
    min= sys.maxsize
    for k in range(i,j):
        count=matrixmultiplication(array,i,k)+matrixmultiplication(array,k+1,j)+array[i-1]*array[k]*array[j]
        if count<min:
            min=count
    return count

print(matrixmultiplication([1,2,3,4,3],1,4))