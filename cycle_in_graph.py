# first iteration
# O(e * v) time | O(v) space
# where v is the number of nodes/vertices in the graph
# and e is the number of edges
def cycleInGraph(edges):
    # Write your code here.
    # graph traversal problem
    for _idx, edge in enumerate(edges):
        stack = [*edge]
        visited_nodes = []
        while stack:
            outbound_idx = stack.pop()
            if outbound_idx == _idx:
                return True
            visited_nodes.append(outbound_idx)
            new_additions = [elem for elem in edges[outbound_idx] if elem not in visited_nodes and elem not in stack]
            stack.extend(new_additions)
    return False


edges = [
    [1, 2],
    [2],
    [1]
  ]
cycleInGraph(edges)