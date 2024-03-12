class Queue:
    class _Node:
        def __init__(self, value=None, next=None) -> None:
            self.value = value
            self.next = next

    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, x):
        new = self._Node(x)
        if self.is_empty():
            self.rear = new
            self.front = new
        else:
            self.rear.next = new
            self.rear = new
        self.size += 1
        return x

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is already empty!")
        temp = self.front
        self.front = self.front.next
        self.size -= 1
        return temp.value

    def peek(self):
        return self.front.value


test = Queue()
test.enqueue(1)
test.enqueue(2)
test.enqueue(3)
print(test.peek())
test.dequeue()
print(test.peek())
