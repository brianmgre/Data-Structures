class Heap:
    def __init__(self):
        self.size = 0
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self.size += 1
        self._bubble_up(self.size - 1)

    def delete(self):
        delete_value = self.storage[0]
        self.storage.pop(0)
        self.size -= 1
        self._sift_down(0)
        return delete_value

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return self.size

    def _bubble_up(self, index):

        while (index - 1)//2 >= 0:
            if self.storage[(index - 1)//2] < self.storage[index]:
                self.storage[index], self.storage[(
                    index - 1)//2] = self.storage[(index - 1)//2], self.storage[index]
            index = (index - 1)//2

    def _sift_down(self, index):
        while index * 2 + 1 <= (self.size - 1):
            if index * 2 + 2 > (self.size - 1):
                max = index * 2 + 1
            elif self.storage[index * 2 + 1] > self.storage[index * 2 + 2]:
                max = index * 2 + 1
            else:
                max = index * 2 + 2
            if self.storage[max] > self.storage[index]:
                self.storage[max], self.storage[index] = self.storage[index], self.storage[max]
            index = max
