def collisionEffects(stack, elem):
    while stack:
        if stack[-1] > 0 and stack[-1] > abs(elem):
            # this is where the bigger asteroid with a positive number
            # is moving right on a collision course.
            return stack
        elif stack[-1] > 0 and stack[-1] == abs(elem):
            # this is where the asteroids coming from both directions
            # on a collision course have the same size.
            stack.pop()
            return stack
        elif stack[-1] > 0 and stack[-1] < abs(elem):
            # this is where the bigger asteroid with a negative number
            # is moving left on a collision course.
            stack.pop()
            stack = collisionEffects(stack, elem)
            return stack
        else:
            stack.append(elem)
            return stack
    return [elem]


# first iteration
# O(n) time and O(n) space
# room for lot of code refactoring
def collidingAsteroids(asteroids):
    # Write your code here.
    stack = []
    for elem in asteroids:
        if not stack or not (stack[-1] > 0 and elem < 0):
            stack.append(elem)
        else:
            # this is the case where
            # asteroid with a positive number is moving right and
            # an asteroid with a negative number is moving left on a collision course
            stack = collisionEffects(stack, elem)
    return stack


asteroids = [1, 2, 3, -4]
print(collidingAsteroids(asteroids))