def remove(array):
    if array == []:
        return 0
    n = len(array)
    i = 0
    j = 0
    map = {}
    for i in range(n):
        if j==n-1:
            break
        if array[i] not in map:
            map[array[i]] = 0
        else:
            if i + 1 < len(array):
                if array[i + 1] not in map:
                    map[array[i + 1]] = 0
                    array[i], array[i + 1] = array[i + 1], array[i]
                    j = i + 1
                else:
                    while j < len(array):
                        if array[j] not in map:
                            map[array[j]] = 0
                            array[i], array[j] = array[j], array[i]
                            break
                        else:
                            j += 1

    count=0
    print(array)
    for j in range(i,n):
        count+=1
    return n-count

print(remove([1,1]))
