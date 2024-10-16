# first iteration
# O(hw) time and O(hw) space
# where h is the height of the graph and
# where w is the width of the graph
def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    edits = [[1 for x in range(1, width + 1)] for y in range(1, height + 1)]
    edits[0][0] = 0

    for i in range(1, height):
        for j in range(1, width):
            edits[i][j] = edits[i-1][j] + edits[i][j-1]
    return edits[-1][-1]


width = 4
height = 3
numberOfWaysToTraverseGraph(width, height)
