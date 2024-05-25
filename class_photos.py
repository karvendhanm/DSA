def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort()
    blueShirtHeights.sort()

    if blueShirtHeights[0] > redShirtHeights[0]:
        redShirtHeights, blueShirtHeights = blueShirtHeights, redShirtHeights

    for _idx, red_height in enumerate(redShirtHeights):
        if red_height <= blueShirtHeights[_idx]:
            return False

    return True


redShirtHeights = [5, 8, 1, 3, 4]
blueShirtHeights = [6, 9, 2, 4, 5]

classPhotos(redShirtHeights, blueShirtHeights)
