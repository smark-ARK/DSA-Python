def sort(arr: list, low: int, high: int):
    if low < high:
        p = partition(arr, low, high)
        sort(arr, low, p - 1)
        sort(arr, p + 1, high)


def partition(arr: list, low: int, high: int):
    pivot = arr[high]
    i, j = low, low
    while i <= high:
        if arr[i] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
        i += 1
    return j - 1


arr = [1, 4, 3, 2, 5]
sort(arr, 0, len(arr) - 1)
print(arr)
