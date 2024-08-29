def sweetAndSavory(dishes, target):
    # Write your code here.
    sweets = []
    savouries = []
    for dish in dishes:
        if dish < 0:
            sweets.append(dish)
        else:
            savouries.append(dish)

    if not len(sweets) or not len(savouries):
        return [0, 0]

    sweets.sort()
    savouries.sort()

    best_combination = None
    sweet_idx, savoury_idx = 0, 0
    while sweet_idx < len(sweets) & savoury_idx < len(savouries):
        combination_target = sweets[sweet_idx] + savoury_idx[savoury_idx]
        if combination_target > target:
            print('the dish is too savoury w.r.t target')

    return []


dishes = [2, 5, -4, -7, 12, 100, -25]
target = -20

sweetAndSavory(dishes, target)