# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def multiply(a, b):
    return a * b


def quotient(a, b):
    return int(a / b)


def addition(a, b):
    return a + b


def subtract(a, b):
    return a - b


_dict = {-1: addition, -2: subtract, -3: quotient, -4: multiply}


def evaluateExpressionTree(tree):
    # Write your code here.
    return evaluateExpressionTreeHelper(tree)


def evaluateExpressionTreeHelper(tree):
    immediate_root_val = tree.value

    if tree.left is None and tree.right is None:
        return immediate_root_val

    left_val = evaluateExpressionTreeHelper(tree.left)
    right_val = evaluateExpressionTreeHelper(tree.right)

    return _dict[immediate_root_val](left_val, right_val)

