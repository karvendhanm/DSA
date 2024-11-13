# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    # O(n) time | O(1) space
    def buildHeap(self, array):
        # Write your code here.
        ParentNodeIndex = (len(array) - 2) // 2
        while ParentNodeIndex >= 0:
            self.siftDown(array, ParentNodeIndex)
            ParentNodeIndex -= 1
        return array

    # O(log n) time | O(1) space
    def siftDown(self, array, idx):
        # Write your code here.

        childPos = (2 * idx) + 1
        childOneIndex = childPos if childPos <= len(array) - 1 else -1
        childTwoIndex = (childPos + 1) if (childPos + 1) <= len(array) - 1 else -1

        if childOneIndex == -1:
            return

        if childTwoIndex == -1:
            if array[childOneIndex] < array[idx]:
                array[childOneIndex], array[idx] = array[idx], array[childOneIndex]
                self.siftDown(array, childOneIndex)
        else:
            if array[childOneIndex] <= array[childTwoIndex] and array[childOneIndex] < array[idx]:
                array[childOneIndex], array[idx] = array[idx], array[childOneIndex]
                self.siftDown(array, childOneIndex)
            elif array[childTwoIndex] <= array[childOneIndex] and array[childTwoIndex] < array[idx]:
                array[childTwoIndex], array[idx] = array[idx], array[childTwoIndex]
                self.siftDown(array, childTwoIndex)

        return

    # O(log n) time | O(1) space
    def siftUp(self, array, idx):
        # Write your code here.
        parentNodeIdx = ((idx - 1) // 2) if ((idx - 1) // 2) >= 0 else -1

        if parentNodeIdx == -1:
            return

        if array[idx] < array[parentNodeIdx]:
            array[idx], array[parentNodeIdx] = array[parentNodeIdx], array[idx]
            self.siftUp(array, parentNodeIdx)

        return

    # O(1) time | O(1) space
    def peek(self):
        # Write your code here.
        return self.heap[0]

    # O(log n) time | O(1) space
    def remove(self):
        # Write your code here.
        # removing the minimum element in the min. heap
        heapLength = len(self.heap)
        self.heap[0], self.heap[heapLength - 1] = self.heap[heapLength - 1], self.heap[0]
        removedElement = self.heap.pop()
        self.siftDown(self.heap, 0)
        return removedElement

    # O(log n) time | O(1) space
    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
        self.siftUp(self.heap, len(self.heap) - 1)


array = [-7, 2, 3, 8, -10, 4, -6, -10, -2, -7, 10, 5, 2, 9, -9, -5, 3, 8]
minHeap = MinHeap(array)
minHeap.insert(-8)
