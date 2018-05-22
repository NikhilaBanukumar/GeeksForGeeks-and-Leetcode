def strStr(haystack, needle):
    if needle in haystack:
        i = 0
        j = 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] != needle[j] and j == 0:
                i += 1
            elif haystack[i] != needle[j] and j != 0:
                i=(i-j)+1
                j = 0
            else:
                i += 1
                j += 1
        return i - (len(needle))
    else:
        return -1
print(strStr("missiissippi","issip"))