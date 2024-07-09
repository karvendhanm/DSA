# first iteration
# O(n^2) time | O(1) space
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    difference = float('inf')
    _lst = []
    for num1 in arrayOne:
        for num2 in arrayTwo:
            if abs(num1 - num2) < difference:
                difference = abs(num1 - num2)
                _lst = [num1, num2]
    return _lst


arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]
print(smallestDifference(arrayOne, arrayTwo))