# first iteration
# O(n ^ 2) time | O(n) space
def balancedBrackets(string):
    # Write your code here.
    brackets = ""
    string = list(string)
    for bracket in string:
        if bracket == "(":
            brackets = brackets + 'A'
        elif bracket == "{":
            brackets = brackets + 'B'
        elif bracket == "[":
            brackets = brackets + 'C'
        elif bracket == ")":
            if brackets == "" or brackets[-1] != 'A':
                return False
            brackets = brackets[:-1]
        elif bracket == "}":
            if brackets == "" or brackets[-1] != 'B':
                return False
            brackets = brackets[:-1]
        elif bracket == "]":
            if brackets == "" or brackets[-1] != 'C':
                return False
            brackets = brackets[:-1]
    if brackets == "":
        return True
    return False


string = "([])(){}(())()()"
balancedBrackets(string)
