# first iteration
# O(n^2) time and O(n) space
# sub-optimal time complexity
def validStartingCity(distances, fuel, mpg):
    # Write your code here.
    mileage = list(map(lambda x: x * mpg, fuel))
    numCities = len(distances)

    for _idx in range(numCities):
        new_distances = distances[_idx:] + distances[:_idx]
        new_mileage = mileage[_idx:] + mileage[:_idx]
        cumsum = 0
        for index, (dist, mil) in enumerate(zip(new_distances, new_mileage)):
            cumsum += (mil - dist)
            if cumsum < 0:
                break
            elif cumsum == 0 and index == numCities - 1:
                return _idx
    return -1


distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10
validStartingCity(distances, fuel, mpg)