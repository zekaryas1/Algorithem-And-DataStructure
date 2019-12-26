from Libraries.Stack_Queue_Linkedlist.LinkedList.Node import Node


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enQueue(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            current_node = Node(value)
            self.tail.next = current_node
            self.tail = current_node

    def deQueue(self):
        data = None
        if self.head is not None:
            data = self.head.data
            self.head = self.head.next
        return data

    def isEmpty(self):
        return self.head is None


if __name__ == '__main__':
    testQueue = Queue()
    print(testQueue.isEmpty())
    testQueue.enQueue(1)
    testQueue.enQueue(2)
    testQueue.enQueue(3)
    print(testQueue.deQueue())
    print(testQueue.deQueue())
    print(testQueue.deQueue())
    print(testQueue.isEmpty())
