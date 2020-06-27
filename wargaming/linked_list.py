
class Node(object):
    __slots__ = ['value', 'next_node', ]

    def __init__(self, value=None):
        self.value = value
        self.next_node = None

    def __repr__(self):
        return str(self.value)


class LinkedList(object):
    __slots__ = ['head', ]

    def __init__(self):
        self.head = None

    def __contains__(self, value):
        last_node = self.head
        while last_node:
            if value == last_node.value:
                return True
            else:
                last_node = last_node.next_node
        return False

    def __repr__(self):
        s = ''
        if self.head is None:
            return s
        last_node = self.head
        while last_node:
            s += last_node.__repr__() + ' '
            last_node = last_node.next_node
        return s

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = new_node

    def __getitem__(self, index):
        last_node = self.head
        i = 0
        while i <= index:
            if i == index:
                return last_node.value
            i = i + 1
            last_node = last_node.next_node

    def remove_first_by_value(self, value):
        head_node = self.head
        if head_node is not None:
            if head_node.value == value:
                self.head = head_node.next_node
                head_node = None
                return
        while head_node is not None:
            if head_node.value == value:
                break
            last_node = head_node
            head_node = head_node.next_node
        if head_node is None:
            return
        last_node.next_node = head_node.next_node
        head_node = None
