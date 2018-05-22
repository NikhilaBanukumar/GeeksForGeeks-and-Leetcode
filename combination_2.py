def calculate(array,new,target,main):
    if target == 0:
        b = list(new)
        main.append(b)
        return
    if target < new[len(new)-1]:
        return
    for j in range(1,len(array)):
        tar =target-array[j]
        if tar >=0:
            new.append(array[j])
            # a[j]=True
            calculate(array[j:],new,tar,main)
            new.pop()
    return

def get_combo(array,target):
    main=[]
    array.sort()
    n=len(array)
    # a=[False for i in range(n)]
    for i in range(n):
        # if a[i]==False:
        #     a[i] = True
        new=[array[i]]
        calculate(array[i:],new,target-array[i],main)
    print(main)

get_combo([1,2,7,6,1,5,10],10)


