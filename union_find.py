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


# solution 2
class UnionFind:
    def __init__(self):
        self.parents = {}
        self.rank = {}

    # O(1) time and O(1) space
    def createSet(self, value):
        self.parents[value] = value
        self.rank[value] = 0

    # O(log n) time and O(1) space
    def find(self, value):
        # we are normally finding the parent or
        # the representative element in the set.
        if value not in self.parents:
            return None

        while value != self.parents[value]:
            value = self.parents[value]
        return value

    # O(log n) time and O(1) space
    def union(self, valueOne, valueTwo):
        if valueOne not in self.parents or valueTwo not in self.parents:
            return

        valueOneParent = self.find(valueOne)
        valueTwoParent = self.find(valueTwo)
        rankParentOne = self.rank[valueOneParent]
        rankParentTwo = self.rank[valueTwoParent]

        if rankParentOne > rankParentTwo:
            self.parents[valueTwoParent] = valueOneParent
            self.rank[valueOneParent] += 1
        else:
            self.parents[valueOneParent] = valueTwoParent
            self.rank[valueTwoParent] += 1

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
