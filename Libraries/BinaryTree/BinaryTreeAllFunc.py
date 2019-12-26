class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def getParent(self):
        return self.parent


def insert(root, t):
    new = Node(t)
    if root is None:
        root = new
    else:
        node = root
        while True:
            if t < node.key:
                # go left
                if node.left == None:
                    node.left = new
                    node.parent = node
                    break
                node = node.left
            else:
                # go right
                if node.right is None:
                    node.right = new
                    node.parent = node
                    break
                node = node.right
    return new


def findMax(root):
    node = root
    while node.right is not None:
        node = node.right
    return node.key


def findMin(root):
    node = root
    while node.left is not None:
        node = node.left
    return node.key


def find(root, t):
    node = root
    if t == node.key:
        return node
    while node is not None:
        if t == node.key:
            return node
        elif t < node.key:
            node = node.left
        else:
            node = node.right
    return node


def get_height(Node):
    if Node == None:
        return 0
    return max(get_height(root.left), get_height(root.right)) + 1


def depth(root, Node):
    if Node == root.key:
        return 0
    else:
        if Node > root.key:
            return 1 + depth(root.right, Node)
        else:
            return 1 + depth(root.left, Node)


if __name__ == '__main__':
    root = Node(60)
    insert(root, 12)
    insert(root, 90)
    insert(root, 4)
    insert(root, 41)

    insert(root, 71)
    insert(root, 100)
    insert(root, 1)
    insert(root, 29)

    insert(root, 84)
    insert(root, 23)
    insert(root, 37)

    # print(findMax(root))
    # print(findMin(root))
    print(depth(root, 37))
