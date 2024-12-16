# O(n^2) time | O(n) space
def sortStack(stack):
    # Write your code here.
    return sortStackHelper(stack)


def sortStackHelper(stack):
    if not stack:
        return stack

    topElem = stack.pop()
    sortStackHelper(stack)

    biggerElements = []
    while stack and stack[-1] > topElem:
        biggerElements.append(stack.pop())
    biggerElements.append(topElem)

    while biggerElements:
        stack.append(biggerElements.pop())

    return stack


stack = [-5, 2, -2, 4, 3, 1]
print(sortStack(stack))
