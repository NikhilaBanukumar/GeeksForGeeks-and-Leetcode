def groupAnagrams(strs):
    main = []
    n = len(strs)
    a = [False for i in range(n)]
    for i in range(n):
        if a[i] != True:
            base = [strs[i]]
            a[i] = True
            for j in range(i+1, n):
                if sorted(strs[i]) == sorted(strs[j]):
                    a[j] = True
                    base.append(strs[j])
            main.append(base)
    print(main)

groupAnagrams(["eat"])
