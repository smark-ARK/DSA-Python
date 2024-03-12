from Queue import Queue


def generate_binary_numbers(n: int):
    res = [None] * n
    q = Queue()
    q.enqueue("1")
    for i in range(n):
        res[i] = q.dequeue()
        q.enqueue(res[i] + "0")
        q.enqueue(res[i] + "1")
    return res


print(generate_binary_numbers(5))
