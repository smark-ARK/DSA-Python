def squares(arr: list, n: int):
    res = [None] * n
    i, j = 0, n - 1

    for k in range(n - 1, -1, -1):
        if abs(arr[i]) > abs(arr[j]):
            res[k] = arr[i] ** 2
            i += 1
        else:
            res[k] = arr[j] ** 2
            j -= 1
    return res


arr = [-4, -2, 0, 1, 3, 7]
print(squares(arr, len(arr)))
