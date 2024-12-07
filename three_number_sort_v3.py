# three number sort using mergeSort algorithm.
_dict = {}


def isSwapNecessary(firstArrNumber, secondArrNumber):
    firstNumber = _dict[firstArrNumber]
    secondNumber = _dict[secondArrNumber]

    if firstNumber > secondNumber:
        return 1
    return 0


def sortLeftandRightArr(leftArr, rightArr):
    leftArrLength = len(leftArr)
    rightArrLength = len(rightArr)

    i = j = 0
    sortedArr = []
    for _idx in range(leftArrLength + rightArrLength):
        if not isSwapNecessary(leftArr[i], rightArr[j]):
            sortedArr.append(leftArr[i])
            i += 1
        else:
            sortedArr.append(rightArr[j])
            j += 1

        if i == leftArrLength:
            sortedArr.extend(rightArr[j:])
            break
        elif j == rightArrLength:
            sortedArr.extend(leftArr[i:])
            break
    return sortedArr


def mergeSort(array):
    if len(array) <= 1:
        return array

    arrLength = len(array)
    splitLength = arrLength // 2

    leftArr = array[:splitLength]
    rightArr = array[splitLength:]
    sortedLeftArr = mergeSort(leftArr)
    sortedRightArr = mergeSort(rightArr)
    return sortLeftandRightArr(sortedLeftArr, sortedRightArr)


# O(n log n) time | O(n) space
def threeNumberSort(array, order):
    global _dict
    for _idx, orderElem in enumerate(order):
        _dict[orderElem] = _idx

    return mergeSort(array)


array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]
threeNumberSort(array, order)
