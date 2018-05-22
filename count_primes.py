#
# def countPrimes(n):
#     count=0
#     if n>2:
#         count+=1
#     s=set()
#     for i in range(3,n,2):
#         if i not in s:
#             count+=1
#             for j in range(i,int(n/i)+1,2):
#                 s.add(i*j)
#     print(count)

def countPrimes(n):
    if n < 2:
        return 0
    result = [True] * n
    result[0] = result[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if result[i] == True:
            for j in range(i*i,n,i):
                result[j] = [False]
    print(result.count(True))
countPrimes(1500000)
