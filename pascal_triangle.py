import math
def getRow(rowIndex):
    a = []
    for i in range(0,rowIndex+1):
        a.append(int((math.factorial(rowIndex))/(math.factorial(i)*math.factorial(rowIndex-i))))
    print(a)

getRow(2)
