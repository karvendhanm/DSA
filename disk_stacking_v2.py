# second iteration
# O(n^2) time | O(n) space
def diskStacking(disks):
    # Write your code here.
    disks = sorted(disks, key=lambda x: x[2], reverse=False)

    heights = [disk[2] for disk in disks]
    sequences = [-1 for _ in disks]
    maxHeightIndex = 0

    for i in range(1, len(disks)):
        currentDisk = disks[i]
        for j in range(i):
            previousDisk = disks[j]
            if isValidDimensions(currentDisk, previousDisk):
                if heights[j] + currentDisk[2] > heights[i]:
                    heights[i] = heights[j] + currentDisk[2]
                    sequences[i] = j

        if heights[i] > heights[maxHeightIndex]:
            maxHeightIndex = i

    return getSequence(sequences, disks, maxHeightIndex)


def getSequence(sequences, disks, maxHeightIndex):
    sequence = [maxHeightIndex]
    while sequences[maxHeightIndex] != -1:
        sequence.append(sequences[maxHeightIndex])
        maxHeightIndex = sequences[maxHeightIndex]
    return [disks[elem] for elem in sequence[::-1]]


def isValidDimensions(c, p):
    return c[0] > p[0] and c[1] > p[1] and c[2] > p[2]


disks = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 2, 1], [4, 4, 5], [1, 1, 4]]
print(diskStacking(disks))

