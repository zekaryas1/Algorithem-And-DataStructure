class Queue:
    def __init__(self):
        self.__size = 0
        self.__array = []
        self.__front = 0

    def enqueue(self, value):
        self.__array.append(value)
        self.__size += 1

    def isEmpty(self):
        return self.__size == 0

    def __len__(self):
        return self.__size

    def dequeue(self):
        data = self.__array[self.__front]
        self.__array[self.__front] = None
        self.__front += 1
        self.__size -= 1
        return data

    def front(self):
        if self.__front >= len(self.__array):
            raise IndexError("No Item in array ")
        else:
            return self.__array[self.__front]


que = Queue()
que.enqueue(12)
que.enqueue(13)
que.enqueue(14)
que.enqueue(15)

print(len(que))
print(que.dequeue())
print(que.dequeue())
print(que.dequeue())
print("front",que.front())
print(que.dequeue())
print(len(que))
# print(que.front())
