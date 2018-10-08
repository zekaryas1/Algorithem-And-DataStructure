class Heap:
    def __init__(self, capcity):
        self.Array = [None] * capcity
        self.count = 0

    def capacity(self):
        return len(self.Array)

    def __str__(self):
        return str(self.Array)

    def add(self, value):
        self.ensureCapacity()
        self.Array[self.count] = value
        self.count += 1
        self.HeapifyUp()

    def HeapifyUp(self):
        index = self.count-1
        while self.Array[index] < self.Array[self.getParentIndex(index)] and index != 0:
            self.swap(index, self.getParentIndex(index))
            index = self.getParentIndex(index)

    def extract_min(self):
        minElt = self.Array[0]
        self.count -= 1
        self.swap(0, self.count)
        self.Array[self.count+1] = None
        self.HeapifyDown()
        return minElt

    def HeapifyDown(self):
        index = 0
        while self.getLeftChildIndex(index)<self.capacity() and self.getLeftChildIndex(index)!=None:
            smallerelt = self.getLeftChildIndex(index)
            if self.getRightChildIndex(index)<self.capacity() and self.Array[self.getRightChildIndex(index)]!=None:
                if self.Array[self.getLeftChildIndex(index)] > self.Array[self.getRightChildIndex(index)]:
                    smallerelt = self.getRightChildIndex(index)
            # print(index)
            # print(smallerelt)
            if self.Array[index] is None or self.Array[smallerelt] is None:
                break
            if self.Array[index] < self.Array[smallerelt]:
                break
            else:
                self.swap(smallerelt, index)
            index = smallerelt

    def swap(self, indexone, indextwo):
        self.Array[indexone], self.Array[indextwo] = self.Array[indextwo], self.Array[indexone]

    def getParentIndex(self, child):
        return child // 2

    def getLeftChildIndex(self, parrent):
        return 2 * parrent + 1

    def getRightChildIndex(self, parrent):
        return 2 * parrent + 2

    def ensureCapacity(self):
        if (self.count + 2) >= self.capacity():
            self.Array = self.Array + ([None] * 5)


if __name__ == '__main__':
    minHeap = Heap(10)
    minHeap.add(12)
    minHeap.add(13)
    minHeap.add(11)
    minHeap.add(10)
    minHeap.add(5)
    minHeap.add(2)
    for i in range(4):
        print("min ",minHeap.extract_min())
    print(minHeap)
