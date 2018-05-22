def median_3(a,b,c):
    return a+b+c-(max(a,b,c)+min(a,b,c))
def median_4(a,b,c,d):
    return (a+b+c+d-(max(a,b,c,d)+min(a,b,c,d)))/2

def median_two_sorted_arrays(a,b):
    na=len(a)
    nb=len(b)
    mida=int((na-1)/2)
    midb=int((nb-1)/2)
    if na == 0 or nb == 0:
        if nb == 0:
            if na % 2 != 0:
                return a[mida]
            else:
                return (a[mida] + a[mida - 1]) / 2
        else:
            if nb % 2 != 0:
                return b[midb]
            else:
                return (b[midb] + b[midb - 1]) / 2
    if na % 2 != 0:
        amed = a[mida]
    else:
        amed = (a[mida] + a[mida - 1]) / 2
    if nb % 2 != 0:
        bmed = b[midb]
    else:
        bmed = (b[midb] + b[midb - 1]) / 2

    if na==nb and na==2:
        if amed>bmed:
            return (a[0]+b[1])/2
        else:
            return (a[1]+b[0]) / 2
    if na==1:
        if nb==1:
            return (a[0]+b[0])/2
        if nb%2==0:
            return median_3(a[0],b[midb],b[midb-1])
        else:
            return median_4(a[0],b[midb],b[midb-1],b[midb+1])

    if nb==1:
        if na==1:
            return (a[0]+b[0])/2
        if nb%2==0:
            return median_3(b[0],a[mida],a[mida-1])
        else:
            return median_4(b[0],a[mida],a[mida-1],a[mida+1])

    if amed==bmed:
        return amed
    elif amed>bmed:
        return median_two_sorted_arrays(a[:mida+1],b[midb:])
    elif bmed>amed:
        return median_two_sorted_arrays(a[mida:],b[:midb+1])

print(median_two_sorted_arrays([1,2],[1,2,3]))