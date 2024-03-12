from Stack import Stack


def next_greater(arr: list):
    n = len(arr)
    res = [None] * n
    s = Stack()
    for i in range(n - 1, -1, -1):
        while (not s.is_empty()) and s.peek() <= arr[i]:
            s.pop()
        if s.is_empty():
            res[i] = -1
        else:
            res[i] = s.peek()
        s.push(arr[i])
    return res


arr = [4, 7, 3, 4, 8, 1]
print(next_greater(arr))
