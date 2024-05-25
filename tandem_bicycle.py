# def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
#     # Write your code here.
#
#     redShirtSpeeds.sort(reverse=False)
#     blueShirtSpeeds.sort(reverse=fastest)
#
#     total_speed = 0
#     for _idx, speed in enumerate(redShirtSpeeds):
#         total_speed += max(speed, blueShirtSpeeds[_idx])
#
#     return total_speed


# second iteration
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.

    redShirtSpeeds.sort(reverse=False)
    blueShirtSpeeds.sort(reverse=fastest)

    return sum([max(speed, blueShirtSpeeds[_idx]) for _idx, speed in enumerate(redShirtSpeeds)])


redShirtSpeeds = [3, 6, 7, 2, 1]
blueShirtSpeeds = [5, 5, 3, 9, 2]
fastest = False

print(tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest))