class MinHeap:
    def __init__(self,k):
        self.array=[0]
        self.current=0
        self.capacity=k
    def heapifyup(self,i):
        while int(i/2)>0:
            if self.array[i]<self.array[int(i/2)]:
                self.array[i],self.array[int(i/2)]=self.array[int(i/2)],self.array[i]
            i=int(i/2)


    def extractmin(self,i):
        ret=self.array[1]
        self.array[1]=self.array[i]
        self.current-=1
        self.array.pop()
        self.heapifyup(self.current)
        return ret

def sortingusingheap(arr,n,k):
    heap=MinHeap(k+1)
    for i in range(n):
        if i<k+1:
            heap.array.append(arr[i])
            heap.current+=1
            heap.heapifyup(heap.current)
            a=heap.array
        else:
            if arr[i]<heap.array[1]:
                arr[i-(k+1)]=arr[i]
                continue
            ret=heap.extractmin(heap.current)
            a=heap.array
            arr[i-(k+1)]=ret
            heap.array.append(arr[i])
            heap.current+=1
            heap.heapifyup(heap.current)
            a=heap.array
    i=n
    j=k
    while j>=0:
        arr[i-(k+1)]=heap.extractmin(heap.current)
        i+=1
        j-=1
    print(heap.array)
    print(arr)


# simpler code
def sortarray(array,k):
    i=0
    while i<len(array):
        for j in range(i,i+k,1):
            if j+k<len(array):
                array[j],array[j+k]=array[j+k],array[j]
            else:
                return array
        i+=2*k
    return array
    # print(array)

# print(sortarray([3,4,1,2,7,8,6,5],2))
sortingusingheap([3,4,1,2,7,8,6,5],8,2)