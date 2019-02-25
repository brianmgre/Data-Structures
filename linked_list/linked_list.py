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
    # if (self.head == None):
    #   self.head =  Node(value)
    
    # node = self.head
    # while(node):
    #   if(node.next_node == None):
    #     return node
    #   node = node.next_node

    # node = Node(value)
    pass
  def remove_head(self):
    if(self.head == None):
      return None
    else:
      self.head = self.head.next_node

  def contains(self, value):
    pass

  def get_max(self):
    pass
