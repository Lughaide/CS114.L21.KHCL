from sys import stdin, stdout


class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None


def add_node(root, value):
    if root is None:
        return Node(value)
    else:
        if root.data == value:
            return root
        elif root.data < value:
            root.right = add_node(root.right, value)
        else:
            root.left = add_node(root.left, value)
    return root


def count_leaf(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    else:
        return count_leaf(root.left) + count_leaf(root.right)


def node_search(root, key):
    if root is None or root.data == key:
        return root
    if root.data < key:
        return node_search(root.right, key)
    else:
        return node_search(root.left, key)


ini_root = Node()


while True:
    value = int(stdin.readline())
    if value == 0:
        break
    else:
        ini_root = add_node(ini_root, value)

count = count_leaf(ini_root)
stdout.write(str(count))