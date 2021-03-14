import sys


class Node:
    def __init__(self, data=None):
        self.data = data
        self.Next = None


class LinkedList:
    def __init__(self):
        self.Head = None
        self.Tail = None

    def print_list(self):
        out_value = self.Head
        while out_value is not None:
            sys.stdout.write(out_value.data + ' ')
            out_value = out_value.Next
        exit(0)

    def add_head(self, value):
        new_node = Node(value)
        if self.Head is None:
            self.Head = self.Tail = new_node
        else:
            new_node.Next = self.Head
            self.Head = new_node
        return

    def add_tail(self, value):
        new_node = Node(value)
        if self.Head is None:
            self.Head = self.Tail = new_node
        else:
            self.Tail.Next = new_node
            self.Tail = new_node
        return

    def add_after_node(self, key, value):
        key_node = self.Head
        while key_node is not None:
            if key_node.data == key:
                break
            key_node = key_node.Next
        if key_node == self.Tail:
            self.add_tail(value)
        elif key_node is not None:
            new_node = Node(value)
            new_node.Next = key_node.Next
            key_node.Next = new_node
        else:
            self.add_head(value)

    def delete_node(self, key):
        key_node = self.Head
        prev_node = None
        while key_node is not None:
            if key_node.data == key:
                break
            prev_node = key_node
            key_node = key_node.Next
        if key_node is None:
            return
        if key_node == self.Head:
            if key_node == self.Tail:
                self.Head = self.Tail = None
            else:
                self.Head = self.Head.Next
        elif key_node == self.Tail:
            self.Tail = prev_node
            prev_node = prev_node.Next
        else:
            prev_node.Next = key_node.Next

    def delete_all_dupes(self, key):
        key_node = self.Head
        prev_node = None
        while key_node is not None and key_node.data == key:
            self.Head = key_node.Next
            key_node = self.Head
        while key_node is not None:
            while key_node is not None and key_node.data != key:
                prev_node = key_node
                key_node = key_node.Next
            if key_node is None:
                return
            elif key_node is self.Tail:
                self.Tail = prev_node
            prev_node.Next = key_node.Next
            key_node = prev_node.Next
        return

    def delete_head(self):
        if self.Head is None:
            return
        elif self.Head == self.Tail:
            self.Head = self.Tail = None
            return
        else:
            self.Head = self.Head.Next
            return

    def custom_lib(self, values):
        if values[0] == '0':
            self.add_head(values[1])
            return
        elif values[0] == '1':
            self.add_tail(values[1])
            return
        if values[0] == '2':
            self.add_after_node(values[1], values[2])
            return
        elif values[0] == '3':
            self.delete_node(values[1])
            return
        if values[0] == '4':
            self.delete_all_dupes(values[1])
            return
        elif values[0] == '5':
            self.delete_head()
            return
        else:
            self.print_list()


BigList = LinkedList()

for line in sys.stdin:
    BigList.custom_lib(line.split())

