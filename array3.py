class minHeap:
    def __init__(self,k):
        self.array=[0]
        self.capacity=k
        self.currentsize=0

    def heapifyup(self,i):
        while int(i/2)>0:
            if self.array[i][0]<self.array[int(i/2)][0]:
                temp=self.array[i]
                self.array[i]=self.array[int(i/2)]
                self.array[int(i/2)]=temp
            i=int(i/2)

    def findminchild(self,i):
        if i*2+1>self.currentsize:
            return 2*i
        if self.array[2*i][0]>self.array[2*i+1][0]:
            return 2*i+1
        else:
            return 2*i

    def heapifydown(self,currentsize):
        i=1
        while i*2<=currentsize:
            minchild=self.findminchild(i)
            if self.array[i][0]<self.array[minchild][0]:
                temp=self.array[i]
                self.array[i]=self.array[minchild]
                self.array[minchild]=temp
            i=minchild

    def insert(self,tup):
        if self.currentsize==self.capacity:
            if tup[0]>self.array[1][0]:
                self.array[1]=tup
                self.heapifydown(self.currentsize)
            else:
                return
        else:
            self.array.append(tup)
            self.currentsize+=1
            self.heapifyup(self.currentsize)


def createmap(array,k):
    map={}
    for i in range(len(array)):
        if array[i] not in map:
            map[array[i]]=1
        else:
            map[array[i]]+=1
    print(map)
    list=[]
    for i in map:
        a=()
        a=(map[i],i)
        list.append(a)
    print(list)
    heap=minHeap(k)
    for i in list:
        heap.insert(i)
    print(heap.array)
    for i in heap.array:
        if i!=0:
            print(i[1])

array=[3, 1, 4, 4, 5, 2, 6, 1]
createmap(array,3)