# class name:
#     __name="nikhila"
#
#     def changename(self,newname):
#         self.__name=newname
#         print(self.__name)
#
# myname=name()
# print(myname._name__name)
# myname.changename("banukumar")

class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # def __repr__(self):
    #     return "Test a:%s b:%s" % (self.a, self.b)
    #
    # def __str__(self):
    #     return "From str method of Test: a is %s," \
    #            "b is %s" % (self.a, self.b)


# Driver Code
t = Test(1234, 5678)
print(t)  # This calls __str__()
print([t])  # This calls __repr__()



# a="my name is nikhila"
# print(str(a))
# print(repr(a))