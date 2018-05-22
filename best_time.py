def best_time(array):
    if len(array)==0:
        return 0
    if len(array)==1:
        return 0
    mid=int(len(array)/2)
    left=best_time(array[:mid])
    right=best_time(array[mid:])
    mini=min(array[:mid])
    maxi=max(array[mid:])
    return max(left,right,maxi-mini)

print(best_time([7,1,5,3,6,4]))