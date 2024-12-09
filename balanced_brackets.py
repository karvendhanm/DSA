# first iteration
# O(n ^ 2) time | O(n) space
# def balancedBrackets(string):
#     # Write your code here.
#     brackets = ""
#     string = list(string)
#     for bracket in string:
#         if bracket == "(":
#             brackets = brackets + 'A'
#         elif bracket == "{":
#             brackets = brackets + 'B'
#         elif bracket == "[":
#             brackets = brackets + 'C'
#         elif bracket == ")":
#             if brackets == "" or brackets[-1] != 'A':
#                 return False
#             brackets = brackets[:-1]
#         elif bracket == "}":
#             if brackets == "" or brackets[-1] != 'B':
#                 return False
#             brackets = brackets[:-1]
#         elif bracket == "]":
#             if brackets == "" or brackets[-1] != 'C':
#                 return False
#             brackets = brackets[:-1]
#     if brackets == "":
#         return True
#     return False


# second iteration
# O(n) time | O(n) space
# def balancedBrackets(string):
#     # Write your code here.
#     stack = []
#     for bracket in list(string):
#         if bracket == "(":
#             stack.append('A')
#         elif bracket == "{":
#             stack.append('B')
#         elif bracket == "[":
#             stack.append('C')
#         elif bracket == ")":
#             if not stack or stack.pop() != 'A':
#                 return False
#         elif bracket == "}":
#             if not stack or stack.pop() != 'B':
#                 return False
#         elif bracket == "]":
#             if not stack or stack.pop() != 'C':
#                 return False
#     if not stack:
#         return True
#     return False


# third iteration.
# O(n) time | O(n) space.
# refactoring the code further.
def balancedBrackets(string):
    # Write your code here.
    closingBrackets = ")]}"
    openingBrackets = "([{"
    matchingBrackets = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    stack = []
    for char in string:
        if char in openingBrackets:
            stack.append(char)
        elif char in closingBrackets:
            if not stack or stack.pop() != matchingBrackets[char]:
                return False
    return len(stack) == 0


string = "([])(){}(())()()"
balancedBrackets(string)
