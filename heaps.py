class MinHeap:
    def __init__(self,k):
        self.heap = [0]
        self.curIndex = 0
        self.capacity=k

    # New item is inserted at last and then reheapify is done to maintain min heap property
    def reHeapifyUp(self,i):
        while int(i/2) > 0:
          if self.heap[i] < self.heap[int(i/2)]:
             tmp = self.heap[int(i/2)]
             self.heap[int(i/2)] = self.heap[i]
             self.heap[i] = tmp
          i = int(i/2)

    #Insert item into heap
    def insert(self,val):
      self.heap.append(val)
      self.curIndex = self.curIndex + 1
      self.reHeapifyUp(self.curIndex)

    #When ExtractMin is performed
    def reHeapifyDown(self,i):
      while (i*2) <= self.curIndex:
          min = self.minChild(i)
          if self.heap[i] > self.heap[min]:
              tmp = self.heap[i]
              self.heap[i] = self.heap[min]
              self.heap[min] = tmp
          i = min

    def minChild(self,i):
      if i*2+1 > self.curIndex:
          return i*2
      else:
          if self.heap[i*2] < self.heap[i*2+1]:
              return i*2
          else:
              return i*2+1

    def extractMin(self):
      ret = self.heap[1]
      self.heap[1] = self.heap[self.curIndex]
      self.curIndex = self.curIndex-1
      self.heap.pop()
      self.reHeapifyDown(1)
      return ret


heap1 = MinHeap(3)
heap1.insert(9)
heap1.insert(5)
heap1.insert(6)
heap1.insert(2)
heap1.insert(3)
print(heap1.extractMin())
print(heap1.extractMin())
print(heap1.extractMin())
print(heap1.extractMin())
print(heap1.extractMin())