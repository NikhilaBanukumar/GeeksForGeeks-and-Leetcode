def addBinary(a, b):
    if len(b)>len(a):
        dif=len(b)-len(a)
        c=""
        while dif>0:
            c+="0"
            dif-=1
        a=c+a
    elif len(a)>len(b):
        dif=len(a)-len(b)
        c=""
        while dif>0:
            c+="0"
            dif-=1
        b=c+b
    carryover="0"
    c=""
    for i in range(len(a)-1,-1, -1):
        if a[i] =="1" and b[i] == "1":
            if carryover=="0":
                c+="0"
            else:
                c+="1"
            carryover="1"
        elif (a[i] =="1" and b[i] == "0") or (a[i] =="0" and b[i] =="1"):
            if carryover=="0":
                c+="1"
            else:
                c+="0"
                carryover="1"
        else:
            if carryover=="0":
                c+="0"
            else:
                c+="1"
                carryover="0"
    if carryover!=0:
        c+=carryover
    print(c[::-1])
addBinary("0","0")