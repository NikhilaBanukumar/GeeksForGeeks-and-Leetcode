class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, x):
        self.min.append(x)
        self.min.sort()
        self.stack.append(x)

    def pop(self):
        if self.stack[len(self.stack) - 1] == self.min[0]:
            self.min.pop(0)
        self.stack.pop()

    def top(self):
        return self.stack[len(self.stack) - 1]

    def getMin(self):
        return self.min[0]

a=MinStack()
a.push(-2)
a.push(0)
a.push(-3)
print(a.getMin())
a.pop()
print(a.stack)
print(a.min)
