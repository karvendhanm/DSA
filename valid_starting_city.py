# first iteration
# O(n^2) time and O(n) space
# sub-optimal time complexity
# def validStartingCity(distances, fuel, mpg):
#     # Write your code here.
#     mileage = list(map(lambda x: x * mpg, fuel))
#     numCities = len(distances)
#
#     for _idx in range(numCities):
#         new_distances = distances[_idx:] + distances[:_idx]
#         new_mileage = mileage[_idx:] + mileage[:_idx]
#         cumsum = 0
#         for index, (dist, mil) in enumerate(zip(new_distances, new_mileage)):
#             cumsum += (mil - dist)
#             if cumsum < 0:
#                 break
#             elif cumsum == 0 and index == numCities - 1:
#                 return _idx
#     return -1


# second iteration
# O(n^2) time and O(1) space
# sub-optimal time complexity
def validStartingCity(distances, fuel, mpg):
    # Write your code here.
    mileage = list(map(lambda x: x * mpg, fuel))
    numCities = len(distances)

    for _idx in range(numCities):
        cumSum = 0
        for _idx1, i in enumerate(range(_idx, numCities + _idx)):
            _idx2 = i % numCities
            cumSum += mileage[_idx2] - distances[_idx2]
            if cumSum < 0:
                break
            elif cumSum == 0 and _idx1 == numCities - 1:
                return _idx
    return -1



distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10
validStartingCity(distances, fuel, mpg)