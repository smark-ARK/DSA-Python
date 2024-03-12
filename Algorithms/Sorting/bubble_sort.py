def bubble_sort(arr: list, n):
    for i in range(n - 1, 0, -1):
        swap = False
        for j in range(i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        if not swap:
            break


arr = [2, 3, 1, 4, 5]
bubble_sort(arr, len(arr))
print(arr)
