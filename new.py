
def lengthOfLongestSubstring( s):
    ch=[-1]*256
    max=0
    ch[ord(s[0])-ord("a")]=0
    current_len=1
    for i in range(1,len(s)):
        prev=ch[ord(s[i])-ord("a")]
        if prev==-1:
            current_len+=1
        else:
            if current_len>max:
                max=current_len
            current_len=i-prev
        ch[ord(s[i])-ord("a")]=i
    if current_len>max:
        max=current_len
    print(max)

s="abbbbbbcghhjkl"
# lengthOfLongestSubstring(s)

for i in range(1,2):
    print(i)