# first iteration
# O(n^2) time | O(n) space
def sweetAndSavory(dishes, target):
    # Write your code here.
    sweets, savouries = [], []
    # this for costs O(n) in time complexity.
    for dish in dishes:
        if dish < 0:
            sweets.append(dish)
        else:
            savouries.append(dish)

    best_combination = [0, 0]
    if not len(sweets) or not len(savouries):
        return best_combination

    # sorting costs O(n log(n)) in time complexity.
    sweets.sort()
    savouries.sort()

    # this double for loop costs O(n^2) time
    for savory in savouries:
        for sweet in sweets:
            combination_score = savory + sweet
            if combination_score <= target:
                if best_combination == [0, 0]:
                    best_combination = [sweet, savory]
                    continue
                _left = target - combination_score
                _right = target - sum(best_combination)
                if _left < _right:
                    best_combination = [sweet, savory]
    return best_combination


dishes = [2, 5, -4, -7, 12, 100, -25]
target = -20

sweetAndSavory(dishes, target)
