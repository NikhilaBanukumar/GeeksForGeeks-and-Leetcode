def pallindrome(string,i,j):
    l=i
    for k in range(j,i,-1):
        if string[l]!=string[k]:
            return False
        l+=1
    return True


def count_strings_added_front(string):
    i=0
    count=0
    for j in range(len(string)-1,i,-1):
        pallin=pallindrome(string,i,j)
        if not pallin:
            count+=1
        else:
            break
    return count
print(count_strings_added_front("AACECAAAAA"))