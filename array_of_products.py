# first iteration
# O(n^2) time | O(n) space
def arrayOfProducts(array):
    # Write your code here.
    product = []
    for _idx, num in enumerate(array):
        i = 0
        prod = 1
        while i < len(array):
            if i != _idx:
                prod *= array[i]
            i += 1
        product.append(prod)
    return product
