class ArrayStack:
    def __init__(self):
        self.array = []
        self.Currentmin = 0
        self.minList = []
    def push(self,value):
        self.setMin(value)
        self.array.append(value)
    def setMin(self,value):
        if len(self.array)==0:
            self.Currentmin = value
            self.minList.append(value)
        elif value<=self.Currentmin:
            self.Currentmin = value
            self.minList.append(value)
    def minValue(self):
        return self.minList[-1]
    def isEmpty(self):
        return len(self.array)==0
    def peak(self):
        return self.array[-1]
    def pop(self):
        data = self.array.pop()
        if data==self.Currentmin:
            self.minList.pop()
        return data
    def __len__(self):
        return len(self.array)

stack = ArrayStack()
stack.push(4)
stack.push(2)
stack.push(3)
stack.push(1)
stack.push(1)
stack.push(1)

print(stack.pop())
print(stack.pop())

print(stack.minValue())

