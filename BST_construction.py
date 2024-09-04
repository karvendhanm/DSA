# first iteration
class BST(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right

        return self

    def contains(self, value):
        currentNode = self
        while currentNode is not None:

            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False

    @staticmethod
    def find_min(node):
        while node.left is not None:
            node = node.left
        return node

    def remove(self, value):
        if self is not None:
            if value < self.value:
                self.left = self.left.remove(value)
            elif value > self.value:
                self.right = self.right.remove(value)
            else:  # value and the currentNode.value matches.
                if self.left is not None and self.right is None:
                    self.value = self.left.value
                    self.left = self.left.left
                elif self.left is None and self.right is not None:
                    self.value = self.right.value
                    self.right = self.right.right
                elif self.left is None and self.right is None:
                    self = None
                elif self.left is not None and self.right is not None:
                    # case where the node has children on both its sides
                    min_node = self.find_min(self.right)
                    self.value = min_node.value
                    self.right = self.right.remove(min_node.value)
        return self


rootNode = BST(1).insert(2).insert(3).insert(4)
rootNode = rootNode.remove(1)
