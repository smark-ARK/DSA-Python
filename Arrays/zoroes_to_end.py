def zeroes_to_end(arr: list):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0 and arr[j] == 0:
            arr[i], arr[j] = arr[j], arr[i]
        if arr[j] != 0:
            j += 1
    return arr


arr = [0, 1, 3, 4, 0, 7, 0, 9, 8]
print(zeroes_to_end(arr))
