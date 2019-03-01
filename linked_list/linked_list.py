"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):

        if not self.head:
            return None

        elif not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None

            return head.value

        else:
            head = self.head
            self.head = self.head.next_node

            return head.value

    def contains(self, value):
        if not self.head:
            return None
        current_node = self.head
        while current_node:

            if value == current_node.get_value():
                return True

            current_node = current_node.get_next()

        return False

    def get_max(self):

        current_node = self.head
        max_value = 0

        while current_node:
            if max_value < current_node.value:
                max_value = current_node.value
            current_node = current_node.next_node

        if max_value == 0:
            return None
        else:
            return max_value
