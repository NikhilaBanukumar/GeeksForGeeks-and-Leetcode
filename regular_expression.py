cache = {}
def isMatch(s, p):
    if (s, p) in cache:
        return cache[(s, p)]
    if not p:
        return not s
    if p[-1] == '*':
        if isMatch(s, p[:-2]):
            cache[(s, p)] = True
            return True
        if s and (s[-1] == p[-2] or p[-2] == '.') and isMatch(s[:-1], p):
            cache[(s, p)] = True
            return True
    if s and (p[-1] == s[-1] or p[-1] == '.') and isMatch(s[:-1], p[:-1]):
        cache[(s, p)] = True
        return True
    cache[(s, p)] = False
    return False

print(isMatch("aabcd",".*bcd"))