import sys
#sys.path.append('../linked_list')
#from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = []

  def enqueue(self, item):
    self.storage.append(item)
  
  def dequeue(self):
    if len(self.storage) == 0:
      return None
    else:
      return self.storage.pop(0)

  def len(self):
    return len(self.storage)
