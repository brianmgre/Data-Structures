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

        new_node = ListNode(value)

        if not self.head:
            self.head = new_node
            self.head = new_node

        else:
            self.tail.insert_after(new_node)
            self.tail = new_node
            self.tail = self.tail.prev

    def remove_from_tail(self):
        if not self.head:
            return None

        elif not self.head.next:
            head = self.head
            self.head = None
            self.tail = None
            return head.value
        else:
            tail = self.tail
            self.tail = self.tail.prev
            return tail.value

    def move_to_front(self, node):
        pass

    def move_to_end(self, node):
        pass

    def delete(self, node):
        pass

    def get_max(self):
        pass
