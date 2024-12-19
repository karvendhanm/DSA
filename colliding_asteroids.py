# def collisionEffects(stack, asteroid):
#     while stack:
#         if stack[-1] > 0 and stack[-1] > abs(asteroid):
#             # this is where the bigger asteroid with a positive number
#             # is moving right on a collision course.
#             return stack
#         elif stack[-1] > 0 and stack[-1] == abs(asteroid):
#             # this is where the asteroids coming from both directions
#             # on a collision course have the same size.
#             stack.pop()
#             return stack
#         elif stack[-1] > 0 and stack[-1] < abs(asteroid):
#             # this is where the bigger asteroid with a negative number
#             # is moving left on a collision course.
#             stack.pop()
#             stack = collisionEffects(stack, asteroid)
#             return stack
#         else:
#             stack.append(asteroid)
#             return stack
#     return [asteroid]
#
#
# # first iteration
# # O(n) time and O(n) space
# # room for lot of code refactoring
# def collidingAsteroids(asteroids):
#     # Write your code here.
#     stack = []
#     for asteroid in asteroids:
#         if not stack or not (stack[-1] > 0 and asteroid < 0):
#             stack.append(asteroid)
#         else:
#             # this is the case where
#             # asteroid with a positive number is moving right and
#             # an asteroid with a negative number is moving left on a collision course
#             stack = collisionEffects(stack, asteroid)
#     return stack


# second iteration
# O(n) time and O(n) space
def collidingAsteroids(asteroids):
    stack = []
    for asteroid in asteroids:
        while stack and stack[-1] > 0 > asteroid:
            if stack[-1] > -asteroid:
                break
            elif stack[-1] == -asteroid:
                stack.pop()
                break
            elif stack[-1] < -asteroid:
                stack.pop()
        else:
            stack.append(asteroid)

    return stack


asteroids = [-3, 5, -8, 6, 7, -4, -7]
print(collidingAsteroids(asteroids))
