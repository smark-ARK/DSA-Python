def merge(arr1: list, arr2: list):
    n1 = len(arr1)
    n2 = len(arr2)
    res = [None] * (n1 + n2)
    i, j, k = 0, 0, 0
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            res[k] = arr1[i]
            i += 1
        else:
            res[k] = arr2[j]
            j += 1
        k += 1

    while i < n1:
        res[k] = arr1[i]
        i += 1
        k += 1
    while j < n2:
        res[k] = arr2[j]
        j += 1
        k += 1

    return res


arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(merge(arr1, arr2))
