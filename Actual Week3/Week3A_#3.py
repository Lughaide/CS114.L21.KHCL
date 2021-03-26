from sys import stdin, stdout
import collections


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

#Source: https://github.com/ttknguyen/CS114.L22.KHCL/blob/master/Assignment/19520188/Week3-DataStructures/problem3.py
def count_level(root):
    if root is None:
        return 0
    else:
        return max(count_level(root.left), count_level(root.right)) + 1


ini_root = None
ini_list = collections.deque()
while True:
    value = stdin.readline().split()
    if len(value) == 0:
        break
    if value[0] == '3':
        break
    if value[0] == '0':
        ini_list.appendleft(int(value[1]))
    elif value[0] == '1':
        ini_list.append(int(value[1]))
    elif value[0] == '2':
        try:
            ini_list.insert(ini_list.index(int(value[1])) + 1, int(value[2]))
        except ValueError:
            ini_list.appendleft(int(value[2]))


#Warning: It's better to take care of equal values in the list before turning into b_tree
for i in ini_list:
    ini_root = add_node(ini_root, i)

stdout.write(str(count_level(ini_root)))