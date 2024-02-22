def merge_sort(arr: list, start: int, end: int):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)


def merge(arr: list, start, mid, end):
    temp = []
    i, j = start, mid + 1
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        if arr[j] <= arr[i]:
            temp.append(arr[j])
            j += 1
    if i <= mid:
        temp += arr[i : mid + 1]
    if j <= end:
        temp += arr[j : end + 1]

    arr[start : end + 1] = temp


arr = [2, 1, 3, 4, 5]
print(arr)
merge_sort(arr, 0, len(arr) - 1)
print(arr)
