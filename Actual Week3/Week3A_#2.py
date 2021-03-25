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

#Source: https://www.geeksforgeeks.org/level-order-tree-traversal/
def print_level(root):
    if root is None:
        return

    queue = [root]

    while len(queue) > 0:
        stdout.write(str(queue[0].data) + ' ')
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

            
ini_root = None


while True:
    value = int(stdin.readline())
    if value == 0:
        break
    else:
        ini_root = add_node(ini_root, value)

print_level(ini_root)