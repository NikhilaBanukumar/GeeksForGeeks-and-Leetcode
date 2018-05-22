#always for string problems use either size 26 or 128 and also use two for loops for substrings
import sys
from collections import defaultdict
def substring(str,pat):
    len1=len(pat)
    len2=len(str)
    if len2<len1:
        return "Incorrect input"
    hash_pat=defaultdict(int)
    hash_str=defaultdict(int)
    for i in range(len1):
        hash_pat[pat[i]]=0
    for i in range(len1):
        hash_pat[pat[i]]+=1
    for i in range(len2):
        hash_str[str[i]]=0

    start=0
    min=sys.maxsize
    start_min=-1
    count=0
    for j in range(len2):
        hash_str[str[j]]+=1
        if str[j] in hash_pat and hash_str[str[j]]<=hash_pat[str[j]]:
            count+=1
        if count==len1:
            while str[start] not in hash_pat or hash_str[str[start]]>=hash_pat[str[start]]:
                if hash_str[str[start]]>=hash_pat[str[start]]:
                    hash_str[str[start]]-=1
                start+=1
            window= (j-start)+1
            if min>window:
                min=window
                start_min=start
    if start_min==-1:
        return "No window"
    return str[start]



print(substring("this is a test string","tist"))