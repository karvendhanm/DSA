# first iteration
# O(n) time | O(1) space
def moveElementToEnd(array, toMove):
    # Write your code here.
    suitableSpace, i = len(array) - 1, len(array) - 1

    while i >= 0:
        if array[i] == toMove:
            switch(array, i, suitableSpace)
            suitableSpace -= 1
        i -= 1
    return array

    
def switch(array, idx1, idx2):
    if idx1 != idx2:
        array[idx1], array[idx2] = array[idx2], array[idx1]
