from itertools import combinations


# def nonConstructibleChange(coins):
#     # Write your code here.
#     if not len(coins):
#         return 1

#     for i in range(1, sum(coins)+2):
#         for j in range(1, len(coins)+1):
#             combs = list(combinations(coins, j))
#             if i in list(set([sum(comb) for comb in combs])):
#                 break
#             if j == len(coins):
#                 return i


def nonConstructibleChange(coins):
    """

    :param coins:
    :return:
    """
    coins.sort()
    total_sum = 0
    for coin in coins:
        if total_sum+1 < coin:
            break
        total_sum += coin
    return total_sum + 1


coins = [1, 1, 1, 1, 1]
print(nonConstructibleChange(coins))
