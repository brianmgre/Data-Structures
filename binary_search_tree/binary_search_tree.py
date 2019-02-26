class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value and self.left:
            self.left.insert(value)
        elif value < self.value:
            self.left = BinarySearchTree(value)
        elif value > self.value and self.right:
            self.right.insert(value)
        elif value > self.value:
            self.right = BinarySearchTree(value)

    def contains(self, target):
        if self.value == target:
            return True

        if self.value < target and self.right:
            return self.right.contains(target)
        elif self.value > target and self.left:
            return self.left.contains(target)

        return False

    def get_max(self):

        if self.right:
            return self.right.get_max()

        else:
            return self.value
