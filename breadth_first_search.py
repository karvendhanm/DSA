# breadth-first search
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self


    # first iteration
    # O(V + E) time | O(V) space
    # where V is the number of vertices (vertices is nothing but nodes) and
    # E is the number of edges.
    def breadthFirstSearch(self, array):
        # Write your code here.
        queue = [self]

        while queue:
            current = queue.pop(0)
            array.append(current.name)
            queue.extend(current.children)
        return array


E_node = Node('E')
F_node = Node('F')
F_node.addChild('I')
F_node.addChild('J')
B_node = Node('B')
B_node.children.append(E_node)
B_node.children.append(F_node)
C_node = Node('C')
G_node = Node('G')
H_node = Node('H')
G_node.addChild('K')
H_node = Node('H')
D_node = Node('D')
D_node.children.append(G_node)
D_node.children.append(H_node)
rootNode = Node('A')
rootNode.children.append(B_node)
rootNode.children.append(C_node)
rootNode.children.append(D_node)


print(rootNode.breadthFirstSearch([]))





