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
def balancedBrackets(string):
    # Write your code here.
    _lst = []
    string = list(string)
    for bracket in string:
        if bracket == "(":
            _lst.append('A')
        elif bracket == "{":
            _lst.append('B')
        elif bracket == "[":
            _lst.append('C')
        elif bracket == ")":
            if not _lst or _lst.pop() != 'A':
                return False
        elif bracket == "}":
            if not _lst or _lst.pop() != 'B':
                return False
        elif bracket == "]":
            if not _lst or _lst.pop() != 'C':
                return False
    if not _lst:
        return True
    return False


string = "([])(){}(())()()"
balancedBrackets(string)
