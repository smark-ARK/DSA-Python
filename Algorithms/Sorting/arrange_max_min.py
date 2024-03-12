def arrange_max_min(arr: list[int], n: int):
    mindx, maxdx = 0, n - 1
    for i in range(n):
        if i % 2 == 0:
            arr[i] = (arr[maxdx] % 10) * 10 + arr[i]
            maxdx -= 1
        else:
            arr[i] = (arr[mindx] % 10) * 10 + arr[i]
            mindx += 1
    for i in range(n):
        arr[i] //= 10
    return


arr = [1, 2, 3, 4, 5, 6, 7, 8]
arrange_max_min(arr, len(arr))
print(arr)
