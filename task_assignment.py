# O(nlog(n)) time and O(n) space
# where n is the number of tasks.
# O(nlog(n)) as we are sorting the array
def taskAssignment(k, tasks):
    # Write your code here.
    durationToIndices = getDurationToIndices(tasks)
    pairedTasks = []

    sortedTasks = sorted(tasks)
    for _idx in range(k):
        firstElement = sortedTasks[_idx]
        firstElementIndex = durationToIndices[firstElement].pop()   # we take the last element in the list

        secondElement = sortedTasks[len(tasks) - 1 - _idx]
        secondElementIndex = durationToIndices[secondElement].pop()
        pairedTasks.append([firstElementIndex, secondElementIndex])

    return pairedTasks


def getDurationToIndices(tasks):
    durationToIndices = {}
    for _idx, elem in enumerate(tasks):
        if elem in durationToIndices:
            durationToIndices[elem].append(_idx)
        else:
            durationToIndices[elem] = [_idx]
    return durationToIndices


k = 3
tasks = [1, 3, 5, 3, 1, 4]
print(taskAssignment(k, tasks))
