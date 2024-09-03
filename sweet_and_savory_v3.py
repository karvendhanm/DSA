# third iteration
# O(n log n) time | O(n) space
def sweetAndSavory(dishes, target):
    # Write your code here.
    sweets = sorted([dish for dish in dishes if dish < 0], key=abs)
    savories = sorted([dish for dish in dishes if dish > 0])

    best_pair = [0, 0]
    best_pair_diff = float('inf')
    sweet_idx, savory_idx = 0, 0
    while sweet_idx < len(sweets) and savory_idx < len(savories):
        current_pair_val = sweets[sweet_idx] + savories[savory_idx]
        current_pair_diff = target - current_pair_val
        if current_pair_val <= target:
            if current_pair_diff < best_pair_diff:
                best_pair = [sweets[sweet_idx], savories[savory_idx]]
                best_pair_diff = current_pair_diff
            savory_idx += 1
        else:
            sweet_idx += 1
    return best_pair


dishes = [2, 5, -4, -7, 12, 100, -25]
target = -20

sweetAndSavory(dishes, target)
