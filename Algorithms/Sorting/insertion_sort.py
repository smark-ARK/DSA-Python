def insertion_sort(arr: list, n: int):
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp


arr = [2, 3, 1, 4, 5]
insertion_sort(arr, len(arr))
print(arr)
