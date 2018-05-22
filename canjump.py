# def canjump(index,array):
#     if index==len(array)-1:
#         return True
#     if index>len(array)-1:
#         return -1
#     else:
#         for i in range(1,array[index]+1):
#             a=canjump(index+i,array)
#             if a==True:
#                 return True
#             if a==-1:
#                 return False
#         return False
# print(canjump(0,[2,0,0]))

no_of_steps_left= max(10,5)
print(no_of_steps_left)