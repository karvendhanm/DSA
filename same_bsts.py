# first iteration
# O(n^2) time | O(n) space
# In each recursion filtering for element in an array < root and >= root adds to time complexity.
def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    return sameBstsHelper(arrayOne, arrayTwo)


def sameBstsHelper(arrayOne, arrayTwo):
    if not arrayOne and not arrayTwo:
        return True

    if len(arrayOne) != len(arrayTwo) or arrayOne[0] != arrayTwo[0]:
        return False

    root = arrayOne[0]
    arrayOne.pop(0)
    arrayTwo.pop(0)

    left, right = False, False
    left = sameBstsHelper([elem for elem in arrayOne if elem < root], [elem for elem in arrayTwo if elem < root])
    if left:
        right = sameBstsHelper([elem for elem in arrayOne if elem >= root], [elem for elem in arrayTwo if elem >= root])

    return left and right


arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]
print(sameBsts(arrayOne, arrayTwo))
