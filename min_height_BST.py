def get_array_order(array, order):
    if not array:
        return None

    center_elm = len(array)//2
    order.append(array[center_elm])
    get_array_order(array[:center_elm], order)
    get_array_order(array[center_elm+1:], order)

    return None


def createBST(rootNode, order):

    for elem in order:
        rootNode.insert(elem)

    return None


# first iteration
def minHeightBst(array):

    order = []
    get_array_order(array, order)

    rootNode = BST(order[0])
    createBST(rootNode, order[1:])

    return rootNode


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
minHeightBst(array)
