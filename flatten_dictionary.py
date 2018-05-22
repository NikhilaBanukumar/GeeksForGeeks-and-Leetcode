finaldict={}
def flatten_dict(dict,j):
    global finaldict
    a=finaldict
    for i in dict:
        if (j not in finaldict) and j!=None:
            finaldict[j]=[i]
        elif j!=None:
            finaldict[j].append(i)
        if isinstance(dict[i],int):
            if i not in finaldict:
                finaldict[i]=[dict[i]]
            else:
                finaldict[i].append(dict[i])
        else:
            flatten_dict(dict[i],i)
    return


dict={3:{2:{1:5,3:6},7:{5:1,10:90,11:8}},9:{8:10,12:30,9:24}}
flatten_dict(dict,None)
print(finaldict)