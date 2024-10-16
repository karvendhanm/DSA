# first iteration
# O(hw) time and O(hw) space
# where h is the height of the graph and
# where w is the width of the graph
# def numberOfWaysToTraverseGraph(width, height):
#     # Write your code here.
#     edits = [[1 for x in range(width)] for y in range(height)]
#     edits[0][0] = 0
#
#     for i in range(1, height):
#         for j in range(1, width):
#             edits[i][j] = edits[i - 1][j] + edits[i][j - 1]
#     return edits[-1][-1]


# second iteration
# O(hw) time and O(min(h, w) space
# where h is the height of the graph and
# where w is the width of the graph
def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    small = width if width < height else height
    big = width if width >= height else height

    evenEdits = [1 for x in range(small)]
    oddEdits = [1 for x in range(small)]

    for i in range(1, big):
        if i % 2 == 1:
            currentEdits = oddEdits
            previousEdist = evenEdits
        else:
            currentEdits = evenEdits
            previousEdist = oddEdits

        for j in range(1, small):
            currentEdits[j] = currentEdits[j-1] + previousEdist[j]

    return evenEdits[-1] if big%2 == 1 else oddEdits[-1]


width = 4
height = 3
numberOfWaysToTraverseGraph(width, height)
