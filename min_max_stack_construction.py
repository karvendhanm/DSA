# first iteration
# O(1) time | O(n) space
class MinMaxStack:
    def __init__(self):
        self.minMaxStack = []
        self.stack = []

    # O(1) time | O(1) space
    def peek(self):
        # Write your code here.
        return self.stack[-1]

    # O(1) time | O(1) space
    def pop(self):
        # Write your code here.
        self.minMaxStack.pop()
        return self.stack.pop()

    # O(1) time | O(1) space
    def push(self, number):
        # Write your code here.
        newMinMax = {'min': number, 'max': number}
        if self.minMaxStack:
            lastMinMax = self.minMaxStack[-1]
            newMinMax['min'] = min(lastMinMax['min'], number)
            newMinMax['max'] = max(lastMinMax['max'], number)
        self.stack.append(number)
        self.minMaxStack.append(newMinMax)

    # O(1) time | O(1) space
    def getMin(self):
        # Write your code here.
        return self.minMaxStack[-1]['min']

    # O(1) time | O(1) space
    def getMax(self):
        # Write your code here.
        return self.minMaxStack[-1]['max']


obj = MinMaxStack()
obj.push(5)
obj.getMin()
obj.getMax()
obj.peek()
obj.push(7)
obj.getMin()
obj.getMax()
obj.peek()
obj.push(2)
obj.getMin()
obj.getMax()
obj.peek()
obj.pop()
obj.pop()
obj.getMin()
obj.getMax()
obj.peek()
