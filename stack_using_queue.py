def enqueue(number):
    global queue
    q2=[]
    q2.append(number)
    for i in range(len(queue)):
        a=dequeue(queue)
        q2.append(a)
    queue=q2


def dequeue(queue):
    temp=queue[0]
    for i in range(len(queue)-1):
        queue[i]=queue[i+1]
    queue.pop()
    return temp

def top(queue):
    return queue[0]

queue=[]
enqueue(10)
enqueue(20)
enqueue(30)

print(top(queue))