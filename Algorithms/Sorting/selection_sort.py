def selection_sort(arr: list, n: int):
    for i in range(n):
        minn = i
        for j in range(i, n):
            if arr[j] < arr[minn]:
                minn = j
        arr[i], arr[minn] = arr[minn], arr[i]


arr = [2, 3, 1, 4, 5]
selection_sort(arr, len(arr))
print(arr)
