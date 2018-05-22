def multiply(num1, num2):
    map = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    num1 = num1[::-1]
    num2 = num2[::-1]
    count=0
    num_1=0
    j=0
    while j<len(num1):
        num_1=num_1+map[num1[j]]*(pow(10,count))
        count+=1
        j+=1

    count = 0
    num_2 = 0
    j = 0
    while j < len(num2):
        num_2 = num_2 + map[num2[j]] * (pow(10, count))
        count += 1
        j += 1
    print(num_1*num_2)

multiply("123","456")