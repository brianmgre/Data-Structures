"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_head(self, value):
        # chech to see if there is a head already

        if not self.head:
            # if no head then set head and tail to new node
            self.head = ListNode(value)
            self.tail = self.head

        # elements in linked list already
        else:
            # update new node as head and point to previous head and have previous head point to new node
            self.head.insert_before(value)
            self.head = self.head.prev

    def remove_from_head(self):

        # if there is nothing in list return none

        if not self.head:
            return None

        # check to see if there is only one node
        # grab a second reference to our head elements
        # set head and tail to none

        if not self.head.next:
            head = self.head
            self.head = None
            self.tail = None

            return head.value

        # multiple items in linked list
        # remove head and make head.next head

        else:
            head = self.head
            self.head = self.head.next
            return head.value

    def add_to_tail(self, value):
        if not self.tail:
            self.tail = ListNode(value)
            self.head = self.tail

        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next

    def remove_from_tail(self):

        current_tail = self.tail
        self.tail.delete()

        if current_tail.prev:
            self.tail = current_tail.prev
        else:
            self.tail = None
            self.head = None

        return current_tail.value
    

    def move_to_front(self, node):
        node_value = node.value
        if node == self.head:
            return
        else:
            node.delete()
            self.add_to_head(node_value)

    def move_to_end(self, node):
        if node.prev is not None:
            node.prev.next = node.next

        if node.next is not None:
            node.next.prev = node.prev

        self.tail.next = node

        node.prev = self.tail
        node.next = None
        self.tail = node

    def delete(self, node):

        if not self.head and not self.tail:
            return None

        if self.head == self.tail:
            self.head = None
            self.tail = None

        if self.head == node:
            self.head = node.next
            node.delete()

        if self.tail == node:
            self.tail = node.prev
            node.delete()

        else:
            node.delete()

    def get_max(self):
        current_node = self.head
        max_node = 0

        while current_node:
            if current_node.value > max_node:
                max_node = current_node.value
            current_node = current_node.next

        return max_node
