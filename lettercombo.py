def lettercombo(number):
    map={"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
    if len(number)==1:
        return map[number[0]]
    array=lettercombo(number[1:])
    cur=map[number[0]]
    new=[]
    for i in range(len(cur)):
        cur_alpha=cur[i]
        for j in range(len(array)):
            new.append(cur_alpha+array[j])
    return new

print(lettercombo("233896592"))
