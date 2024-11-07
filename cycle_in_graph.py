# first iteration
# O(e * v) time | O(v) space
# where v is the number of nodes/vertices in the graph
# and e is the number of edges
# def cycleInGraph(edges):
#     # Write your code here.
#     # graph traversal problem
#     for _idx, edge in enumerate(edges):
#         stack = [*edge]
#         visited_nodes = []
#         while stack:
#             outbound_idx = stack.pop()
#             if outbound_idx == _idx:
#                 return True
#             visited_nodes.append(outbound_idx)
#             new_additions = [elem for elem in edges[outbound_idx] if elem not in visited_nodes and elem not in stack]
#             stack.extend(new_additions)
#     return False


# second iteration
# O(e + v) time | O(v) space
# where v is the number of nodes/vertices in the graph
# and e is the number of edges
def cycleInGraph(edges):
    # Write your code here.
    numVertices = len(edges)
    visitedNodes = [0 for _ in range(numVertices)]
    currentlyInStack = [0 for _ in range(numVertices)]

    for node in range(numVertices):
        if visitedNodes[node]:
            continue

        isCycleInNode = getIsCycleInGraph(node, edges, visitedNodes, currentlyInStack)
        if isCycleInNode:
            return True

    return False


def getIsCycleInGraph(node, edges, visitedNodes, currentlyInStack):
    visitedNodes[node] = 1
    currentlyInStack[node] = 1
    outboundEdges = edges[node]

    for outboundEdge in outboundEdges:
        if visitedNodes[outboundEdge] and currentlyInStack[outboundEdge]:
            # indicates the presence of a back edge (a cycle)
            return True

        if visitedNodes[outboundEdge]:
            continue

        isCycleInNode = getIsCycleInGraph(outboundEdge, edges, visitedNodes, currentlyInStack)
        if isCycleInNode:
            return True

    currentlyInStack[node] = 0
    return False


edges = [
    [1, 3],
    [2, 3, 4],
    [0],
    [],
    [2, 5],
    []
]
print(cycleInGraph(edges))

#   [
#   [1, 2],
#   [2],
#   [1]
# ]
