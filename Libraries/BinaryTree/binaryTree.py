from Libraries.Stack_Queue_Linkedlist.Stack_And_Queue_With_Node.Queue import Queue


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# deapth first traversal
def preorderTraversal(subtree):
    if subtree is not None:
        print(subtree.data)
        inorderTraversal(subtree.left)
        inorderTraversal(subtree.right)


def inorderTraversal(subtree):
    if subtree is not None:
        inorderTraversal(subtree.left)
        print(subtree.data)
        inorderTraversal(subtree.right)


def postorderTraversal(subtree):
    if subtree is not None:
        inorderTraversal(subtree.left)
        inorderTraversal(subtree.right)
        print(subtree.data)


# breadth first traversal

def BFT(root):
    q = Queue()
    q.enQueue(root)

    while not q.isEmpty():
        node = q.deQueue()
        print(node.data)
        if node.left is not None:
            q.enQueue(node.left)
        if node.right is not None:
            q.enQueue(node.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("preorder Traversal")
    preorderTraversal(root)
    print("inorder Traversal")
    inorderTraversal(root)
    print("postorder Traversal")
    postorderTraversal(root)

    print("BFT")
    BFT(root)
