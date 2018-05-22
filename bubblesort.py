# O(n2)

def bubblesort(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

def optimised(a):
    n=len(a)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                swapped=True
                a[j], a[j + 1] = a[j + 1], a[j]

        if swapped==False:
            break
    return a


a=[5,1,4,2,8]
print(bubblesort(a))
print(optimised(a))


