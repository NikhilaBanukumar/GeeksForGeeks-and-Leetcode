import sys
def integer_to_roman(integer):
    map={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
    y=0
    stri=""
    if integer in map:
        return map[integer]
    while integer>0:
        if integer%10==0:
            integer = int(integer / 10)
            y+=1
            continue
        if y==0:
            current_number=integer%10
            y=1
        else:
            current_number=pow(10,y)*(integer%10)
            y += 1

        z=pow(10, y-1)
        min_max=sys.maxsize
        max_min=0
        if current_number in map:
            stri+=map[current_number]
        else:
            for i in map:
                if current_number>i:
                    if i>max_min:
                        max_min=i
                elif current_number<i:
                    if i<min_max:
                        min_max=i
            if min_max-z==current_number:
                stri+=map[min_max]+map[z]
            else:
                diff=int((current_number-max_min)/z)
                while diff:
                    stri+=map[z]
                    diff-=1
                stri += map[max_min]
        integer=int(integer/10)
    return stri[::-1]

print(integer_to_roman(1001))