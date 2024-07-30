# first iteration
# O(n) time | O(n) space
# def firstDuplicateValue(array):
#     # Write your code here.
#     duplicateDict = {}
#     for _idx, elem in enumerate(array):
#         if elem in duplicateDict:
#             return elem
#         else:
#             duplicateDict[elem] = _idx
#     return -1


# second iteration
# O(n) time | O(n) space
def firstDuplicateValue(array):
    # Write your code here.
    duplicates = set()
    for elem in array:
        if elem in duplicates:
            return elem
        else:
            duplicates.add(elem)
    return -1


# third iteration
# O(n) time | O(n) space
def firstDuplicateValue(array):
    # Write your code here.
    duplicates = {}
    for elem in array:
        if duplicates.get(elem):    # get will return None if the elem is not found in the dictionary.
            return elem
        duplicates[elem] = True
    return -1
