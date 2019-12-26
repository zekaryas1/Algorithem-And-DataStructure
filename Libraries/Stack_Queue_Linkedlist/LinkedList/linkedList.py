# start
from Libraries.Stack_Queue_Linkedlist.LinkedList.Node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def getHead(self):
        return self.head

    def add(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode

    def remove(self, value):
        if self.head.data == value:
            data = self.head.data
            self.head = self.head.next
        else:
            current = self.head
            while current.next.data != value:
                current = current.next
            data = current.next.data
            current.next = current.next.next
        return data

    def __str__(self):
        kl = []
        current = self.head
        while current.next is not None:
            kl.append(current.data)
            current = current.next
        kl.append(current.data)
        return str(kl)


def breakInHalf(head):
    pointer1 = head
    pointer2 = head
    while pointer2.next is not None:
        pointer2 = pointer2.next.next
        if pointer2 is None:
            break
        pointer1 = pointer1.next

    nodes = pointer1.next
    linkedList = LinkedList()
    while nodes.next is not None:
        linkedList.add(nodes.data)
        nodes = nodes.next
    linkedList.add(nodes.data)

    pointer1.next = None

    return linkedList.getHead()


if __name__ == '__main__':
    linkedList = LinkedList()
    linkedList.add(12)
    linkedList.add(13)
    linkedList.add(14)
    linkedList.add(15)
    linkedList.add(16)
    linkedList.add(17)
    # linkedList.add(18)

    # linkedList.add(17)
    print(linkedList)

    headofLinked = breakInHalf(linkedList.getHead())

    print(linkedList)

    while headofLinked.next is not None:
        print(headofLinked.data)
        headofLinked = headofLinked.next
    print(headofLinked.data)
