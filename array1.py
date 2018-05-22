def search_rotated_array(a,key,low,high):
    #given array [5,6,7,8,1,3,4] key=3 works only for rotated arrays
    if low>=high:
        return "Cant find"
    mid=int((low+high)/2)
    if key==a[mid]:
        return mid
    if key<a[mid]:
        if key<a[low]:
            return search_rotated_array(a,key,mid+1,high)
        else:
            return search_rotated_array(a,key,low,mid-1)
    elif key>a[mid]:
        if key<a[low]:
            return search_rotated_array(a,key,mid+1,high)
        else:
            return search_rotated_array(a,key,low,mid)

def search(array,key,low,high):
    if low>high:
        return "Cant Find"
    mid= int((low+high)/2)
    if key==array[mid]:
        return mid
    elif key<array[mid]:
        return search(array,key,low,mid-1)
    else:
        return search(array,key,mid+1,high)


def rotated_search(array,key):
    pivot=pivot_find(array,0,len(array)-1)
    print(pivot)
    if pivot==0:
        return search(array,key,0,len(array)-1)
    if key>array[pivot]:
        return search(array,key,pivot,len(array)-1)
    else:
        return search(array,key,0,pivot-1)



def pivot_find(array,low,high):
    if low>high:
        return -1
    mid=int((low+high)/2)
    if array[mid]==array[high]:
        a=mid
        return a

    if array[mid]<array[high]:
        if array[mid]<array[mid-1]:
            a=mid
            return a
        else:
            return pivot_find(array,low,mid-1)
    else:
        return pivot_find(array,mid+1,high)


# print(search_rotated_array([1,2,3,4,5,6,7],3,0,7))
print(rotated_search([1,2,3,4,5,6,7,8],2))


