from Libraries.Stack_Queue_Linkedlist.LinkedList.Node import Node


class Stack:
    def __init__(self):
        self.head = None

    def add(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = Node(value)
            current_node.next = self.head
            self.head = current_node

    def pop(self):
        data = None
        if self.head is not None:
            data = self.head.data
            self.head = self.head.next
        return data


if __name__ == '__main__':
    testStack = Stack()
    testStack.add(1)
    testStack.add(2)
    testStack.add(3)
    print(testStack.pop())
    print(testStack.pop())
    print(testStack.pop())
    testStack.add(4)
    print(testStack.pop())
