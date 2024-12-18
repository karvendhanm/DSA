# first iteration - recursive solution
# O(n) time | O(n) space
# def arithmetic(a, b, operator):
#     if operator == '+':
#         return a + b
#     elif operator == '-':
#         return a - b
#     elif operator == '*':
#         return a * b
#     elif operator == '/':
#         return int(a / b)
#
#
# def reversePolishNotation(tokens):
#     # Write your code here.
#     while tokens:
#         topElem = tokens.pop()
#         if topElem in "+-*/":
#             secondElem = reversePolishNotation(tokens)
#             firstElem = reversePolishNotation(tokens)
#             return arithmetic(firstElem, secondElem, topElem)
#         return int(topElem)


# second iteration - iterative solution
# O(n) time | O(n) space
def reversePolishNotation(tokens):
    stack = []
    for token in tokens:
        if token in '+-*/':
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  # Ensure integer division
        else:
            stack.append(int(token))
    return stack[0]


tokens = ["4", "-7", "2", "6", "+", "10", "-", "/", "*", "2", "+", "3", "*"]
print(reversePolishNotation(tokens))
