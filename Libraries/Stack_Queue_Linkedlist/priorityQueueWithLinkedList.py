class Node:
    def __init__(self,item,priority):
        self.item = item
        self.priority = priority
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def add(self,item=None,priority=None):
        assert item!=None and priority!=None,'Node data needed'
        if self.head==None:
            self.head=Node(item,priority)
        else:
            node = self.head
            while node.next!=None:
                node = node.next
            node.next = Node(item,priority)
    def remove(self):
        assert self.head!=None,'No item in the LinkedList'
        maxPriority = self.__findMax()
        print('max is ',maxPriority)
        node = self.head
        if node.priority == maxPriority:
            data  = self.head.item
            if self.head.next == None:
                self.head=None
            else:
                self.head = self.head.next
            return data
        while node.next.priority !=maxPriority:
            node = node.next
        data = node.item
        node.next = node.next.next
        return data
    def __findMax(self):
        if self.head==None:
            return
        else:
            node = self.head
            maxPriority = self.head.priority
            while node.next!=None:
                if node.priority>maxPriority:
                    maxPriority = node.priority
                node = node.next
            if node.priority>maxPriority:
                maxPriority = node.priority

        return maxPriority


if __name__ == '__main__':
    priorityQueue = LinkedList()
    priorityQueue.add('apple',20)
    priorityQueue.add('samsung',200)
    priorityQueue.add('nokia',550)
    priorityQueue.add('HA', 400)
    priorityQueue.add('Tecno', 550)
    print(priorityQueue.remove())