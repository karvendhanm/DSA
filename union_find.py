# solution 1
class UnionFind:
    def __init__(self):
        self.parents = {}

    # O(1) time and O(1) space
    def createSet(self, value):
        self.parents[value] = value

    # O(n) time and O(1) space
    def find(self, value):
        if value not in self.parents:
            return None

        currentParent = value
        while currentParent != self.parents[currentParent]:
            currentParent = self.parents[currentParent]

        return currentParent

    # O(n) time | O(1) space
    def union(self, valueOne, valueTwo):
        if valueOne not in self.parents or valueTwo not in self.parents:
            return

        valueOneParent = self.find(valueOne)
        valueTwoParent = self.find(valueTwo)
        if valueOneParent != valueTwoParent:
            self.parents[valueOneParent] = valueTwoParent
        return


obj = UnionFind()
obj.createSet(3)
obj.createSet(6)
obj.find(6)
obj.union(3, 6)
obj.find(3)
obj.find(6)
obj.createSet(2)
obj.union(2, 6)