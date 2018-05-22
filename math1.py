array=[]
med=0
def insert(array,number):
    array1=[]
    for i in range(len(array)):
        if array[i]>number:
            if i==0:
                array1.append(number)
                array1.extend(array[i:len(array)])
                break
            else:
                array1.extend(array[0:i])
                array1.append(number)
                array1.extend(array[i:len(array)])
                break
    return array1

def findmeadian(number):
    global array
    global med
    if array==[]:
        array.append(number)
        med=number
    if number>array[len(array)-1]:
        if len(array)==1:
            med=int((number+array[0])/2)
        elif int(len(array)%2)==0:
            med=array[len(array)/2]
        else:
            med=int(array[int(len(array)/2)]+array[int(len(array)/2)+1]/2)
        array.append(number)

    elif number<array[len(array)-1]:
        array=insert(array,number)
        if len(array)%2==0:
            med=int((array[int(len(array)/2)]+array[int(len(array)/2)-1])/2)
        else:
            med=array[int(len(array)/2)]
    return med
right=[]
left=[]
medsim=0
def simpler(number):
    global medsim
    if number>medsim:
        right.append(number)
    else:
        left.append(number)
    if len(left)==len(right):
        medsim=(right[len(right)-1]+left[len(left)-1])/2
    elif len(left)==len(right)-1:
        medsim=right[len(right)-1]
    elif len(left)<len(right)-1:
        left.append(right.pop())
        medsim=(right[len(right)-1]+left[len(left)-1])/2
    elif len(left)==len(right)+1:
        medsim=left[len(left)-1]
    elif len(right)<len(left)-1:
        right.append(left.pop())
        medsim=(right[len(right)-1]+left[len(left)-1])/2
    print(medsim)
class heap:
    def __init__(self):
        self.array=[0]
        self.current=0
maxheap=heap()
minheap=heap()
med3=0
def heap(number):
    if minheap.array==[] and maxheap.array==[]:
        minheap.array.append(number)
        med=number
    elif number>minheap.array[1]:
        if maxheap.array==[]:
            maxheap.array.append(number)
            maxheap.current+=1
        else:
            minheap.array.append(number)
            minheap.current+=1
            minheap.heapifyup(minheap.current)
    elif number<minheap.array[1]:
        if maxheap.array==[]:
            maxheap.array.append(number)
            maxheap.current+=1
        elif maxheap.array[1]>number:
            ret=maxheap.extractmin()
            maxheap.heapifydown()
            minheap.array.append(ret)
            minheap.current+=1
            minheap.heapifyup(minheap.current)
            maxheap.array.append(number)
            maxheap.current+=1
            maxheap.heapifyup(maxheap.current)
        elif maxheap.array[1]<number:
            maxheap.array.append(number)
            maxheap.current+=1
            maxheap.heapifyup(maxheap.current)
    if maxheap.current==minheap.current:
        med=maxheap.array[maxheap.current]+minheap.array[minheap.current]
    elif minheap.current==maxheap.current+1:
        med=minheap.array[minheap.current]
    elif minheap.current+1==maxheap.current:
        med=maxheap.array[maxheap.current]



simpler(5)
simpler(15)
simpler(1)
# print(findmeadian(3))
# print(findmeadian(0))