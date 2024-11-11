# first iteration sub-optimal time
# O(N * ME) time | O(N) space
# where N is the number of nodes in the graph
# and ME is the maximum number of edges outbound from a node.
# def twoColorable(edges):
#     # Write your code here.
#     colors = ['N' for _ in range(len(edges))]
#     colors_dict = {'W': 'B', 'B': 'W'}
#
#     for node_idx, edge in enumerate(edges):
#         if colors[node_idx] == 'N':
#             colors[node_idx] = 'B'
#
#         for outbound_idx in edge:
#             if colors[outbound_idx] == 'N':
#                 colors[outbound_idx] = colors_dict[colors[node_idx]]
#             elif colors[outbound_idx] != colors_dict[colors[node_idx]]:
#                 return False
#     return True


# second iteration
# key idea - no need to visit the same node twice.
# O(N * E) time | O(N) space
# where N is the number of nodes in the graph
# and E is the maximum number of edges in the graph.
# def twoColorable(edges):
#     # Write your code here.
#     visited = [0 for _ in range(len(edges))]
#     colors = ['N' for _ in range(len(edges))]
#     colors_dict = {'W': 'B', 'B': 'W'}
#
#     for node_idx, edge in enumerate(edges):
#         if colors[node_idx] == 'N':
#             colors[node_idx] = 'B'
#
#         for outbound_idx in edge:
#             if visited[outbound_idx]:
#                 continue
#
#             if colors[outbound_idx] == 'N':
#                 colors[outbound_idx] = colors_dict[colors[node_idx]]
#             elif colors[outbound_idx] != colors_dict[colors[node_idx]]:
#                 return False
#
#         visited[node_idx] = 1
#     return True


# third iteration
# O(N * E) time | O(N) space
# where N is the number of nodes in the graph
# and E is the maximum number of edges in the graph.
def twoColorable(edges):
    # Write your code here.
    colors = [None for _ in edges]
    colors[0] = True
    stack = [0]

    while stack:
        node = stack.pop(0)
        for connection in edges[node]:
            if colors[connection] is None:
                stack.append(connection)
                colors[connection] = not colors[node]
            elif colors[connection] == colors[node]:
                return False
    return True


# edges = [
#     [1, 2],
#     [0, 2],
#     [0, 1]
# ]
# edges = [
#     [2],
#     [2, 3],
#     [0, 1],
#     [1]
#   ]
edges = [
    [1, 4],
    [0, 2, 3],
    [1, 4],
    [1],
    [0, 2]
]
print(twoColorable(edges))