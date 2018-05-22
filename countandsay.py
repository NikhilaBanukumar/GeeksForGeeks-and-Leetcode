def countAndSay( n):
    if n == 0:
        return 0
    s = "1"
    for i in range(1,n):
        prev = None
        new = ""
        for i in range(len(s)):
            if prev == None:
                count = 1
                prev = s[i]
            elif s[i] == prev:
                count += 1
            elif s[i] != prev:
                new += str(count) + prev
                prev = s[i]
                count = 1
        new += str(count) + prev
        s = new
    print(s)

countAndSay(5)