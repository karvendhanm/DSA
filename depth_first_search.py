# depth first search iteration one.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
        array.append(self.name)
        if len(self.children):
            array = self.depthFirstSearchHelper(array)
        return array

    def depthFirstSearchHelper(self, array):
        for item in self.children:
            array.append(item.name)
            if len(item.children):
                array = item.depthFirstSearchHelper(array)
        return array


# depth first search iteration two.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
        array.append(self.name)
        if len(self.children):
            for item in self.children:
                array = item.depthFirstSearch(array)
        return array
