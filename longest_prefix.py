import sys
def longest_preffix(strs):
    min=sys.maxsize
    for i in range(len(strs)):
        if len(strs[i])<min:
            min=len(strs[i])

    st=""
    for i in range(min):
        char=strs[0][i]
        for j in range(1,len(strs)):
            if strs[j][i]==char:
                flag=1
            else:
                flag=0
                break
        if flag==1:
            st+=char
        else:
            return st
    return st

print(longest_preffix([""]))