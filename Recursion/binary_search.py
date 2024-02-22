def binary_search(arr: list, left: int, right: int, x):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == x:
        return mid
    if x < arr[mid]:
        return binary_search(arr, left, mid - 1, x)
    return binary_search(arr, mid + 1, right, x)


arr = [1, 2, 3, 4, 5, 6, 7]
print(binary_search(arr, 0, len(arr) - 1, 7))
