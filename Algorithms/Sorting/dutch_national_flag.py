def dutch_national_flag(arr: list, n: int):
    i, j, k = 0, 0, n - 1
    while i <= k:
        if arr[i] == 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
            i += 1
        elif arr[i] == 1:
            i += 1
        elif arr[i] == 2:
            arr[i], arr[k] = arr[k], arr[i]
            k -= 1


arr = [0, 1, 2, 0, 0, 1, 2]
dutch_national_flag(arr, len(arr))
print(arr)
