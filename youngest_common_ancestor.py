# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


# iteration 1 - suboptimal time complexity
# O(n^2) time and O(1) space
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    if descendantOne == topAncestor or descendantTwo == topAncestor:
        return topAncestor

    currentFirstAncestor = descendantOne
    while currentFirstAncestor is not None:
        currentSecondAncestor = descendantTwo
        while currentSecondAncestor is not None:
            if currentFirstAncestor == currentSecondAncestor:
                return currentFirstAncestor
            currentSecondAncestor = currentSecondAncestor.ancestor
        currentFirstAncestor = currentFirstAncestor.ancestor
    return topAncestor


def getDescendantLevel(topAncestor, descendant):
    level = 0
    while descendant != topAncestor:
        level += 1
        descendant = descendant.ancestor
    return level


def bringUpthelevel(descendant, level):
    for i in range(level):
        descendant = descendant.ancestor
    return descendant


# iteration 2
# O(n) time and O(1) space - worst case
# O(D) time and O(1) space where D is the depth of the lowest node.
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # bringing both the descendandants to the same level
    if descendantOne == topAncestor or descendantTwo == topAncestor:
        return topAncestor

    # O(n) time | O(1) space - worst case
    levelOne = getDescendantLevel(topAncestor, descendantOne)
    # O(n) time | O(1) space - worst case
    levelTwo = getDescendantLevel(topAncestor, descendantTwo)

    if levelOne > levelTwo:
        # O(n) time | O(1) space - worst case
        descendantOne = bringUpthelevel(descendantOne, levelOne-levelTwo)
    elif levelTwo > levelOne:
        # O(n) time | O(1) space - worst case
        descendantTwo = bringUpthelevel(descendantTwo, levelTwo - levelOne)

    # O(n) time | O(1) space - worst case
    while descendantOne != descendantTwo:
        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor

    return descendantOne


top_ancestor = AncestralTree("A")
tree_B = AncestralTree("B")
tree_B.ancestor = top_ancestor

tree_C = AncestralTree("C")
tree_C.ancestor = top_ancestor

tree_D = AncestralTree("D")
tree_D.ancestor = tree_B

tree_E = AncestralTree("E")
tree_E.ancestor = tree_B

tree_F = AncestralTree("F")
tree_F.ancestor = tree_C

tree_G = AncestralTree("G")
tree_G.ancestor = tree_C

tree_H = AncestralTree("H")
tree_H.ancestor = tree_D

tree_I = AncestralTree("I")
tree_I.ancestor = tree_D

obj = getYoungestCommonAncestor(top_ancestor, tree_E, tree_I)
print(obj.name)


