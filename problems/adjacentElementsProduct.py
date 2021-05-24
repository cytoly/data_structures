def adjacentElementsProduct(arr):
    product = arr[0] * arr[1]
    for i in range(len(arr) - 1):
        res = arr[i] * arr[i+1]
        product = res if res >= product else product
    return product