# second iteration
# O(n log n) time | O(n) space
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
    sweets.sort(reverse=True)
    savouries.sort()

    # this while loop costs O(n) time
    sweet_idx, savory_idx = 0, 0
    while sweet_idx < len(sweets) and savory_idx < len(savouries):
        combination_score = sweets[sweet_idx] + savouries[savory_idx]
        if combination_score <= target:
            if combination_score == target:
                return [sweets[sweet_idx], savouries[savory_idx]]
            elif best_combination == [0, 0] or ((target - combination_score) < (target - sum(best_combination))):
                best_combination = [sweets[sweet_idx], savouries[savory_idx]]
        if combination_score < target:
            savory_idx += 1
        else:
            sweet_idx += 1

    return best_combination


dishes = [2, 5, -4, -7, 12, 100, -25]
target = -20

sweetAndSavory(dishes, target)
