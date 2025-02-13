# first iteration
# O(n^2) time | O(n) space
def diskStacking(disks):
    # Write your code here.
    sorted_disks = sorted(disks, key=lambda x: x[2], reverse=False)
    diskStacking = []
    for i in range(len(sorted_disks)):
        height = sorted_disks[i][2]
        diskStacking.append([height, -1])
    maxHeight = sorted_disks[0][2]
    maxHeightIndex = 0
    for i in range(1, len(diskStacking)):
        for j in range(i):
            if (sorted_disks[j][0] < sorted_disks[i][0]
                    and sorted_disks[j][1] < sorted_disks[i][1]
                    and sorted_disks[j][2] < sorted_disks[i][2]):
                if diskStacking[j][0] + sorted_disks[i][2] > diskStacking[i][0]:
                    diskStacking[i][0] = diskStacking[j][0] + sorted_disks[i][2]
                    diskStacking[i][1] = j

            if diskStacking[i][0] > maxHeight:
                maxHeight = diskStacking[i][0]
                maxHeightIndex = i
    return getSequence(diskStacking, maxHeightIndex, sorted_disks)


def getSequence(diskStacking, maxHeightIndex, sorted_disks):
    sequence = [maxHeightIndex]

    while diskStacking[maxHeightIndex][1] != -1:
        sequence.append(diskStacking[maxHeightIndex][1])
        maxHeightIndex = diskStacking[maxHeightIndex][1]

    return [sorted_disks[elem] for elem in sequence[::-1]]


disks = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 2, 1], [4, 4, 5], [1, 1, 4]]
print(diskStacking(disks))
