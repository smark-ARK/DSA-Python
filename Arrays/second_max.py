def second_max(arr: list):
    m = float("-inf")
    sm = float("-inf")
    for i in arr:
        if i > m:
            sm = m
            m = i
        elif i > sm and i != m:
            sm = i
    return sm


arr = [1, 2, 4, 5, 9, 8, 7]
print(second_max(arr))
