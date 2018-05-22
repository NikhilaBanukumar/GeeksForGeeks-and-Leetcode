def same_characters(words):
    map={}
    for word in words:
        word1=sorted(word)
        word1="".join(word1)
        if word1 not in map:
            map[word1]=[]
            map[word1].append(word)
        else:
            map[word1].append(word)
    for i in map:
        print(",".join(map[i]))

same_characters(["may","yam","good","air"])
