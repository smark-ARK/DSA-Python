def missing_number(arr: list):
    n = len(arr) + 1
    summ = (n * (n + 1)) // 2
    for i in arr:
        summ -= i
    return summ


arr = [1, 2, 4, 5, 6, 7]
print(missing_number(arr))
