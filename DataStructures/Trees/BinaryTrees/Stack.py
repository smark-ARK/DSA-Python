class Stack:
    class _Node:
        def __init__(self, value=None, next=None) -> None:
            self.value = value
            self.next = next

    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        new_node = self._Node(x)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.size += 1
        return x

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is Empty!")
        temp = self.top
        self.top = self.top.next
        self.size -= 1
        return temp.value

    def peek(self):
        return self.top.value if self.top else None


test = Stack()
test.push(1)
test.push(2)
test.push(3)
test.pop()
print(test.peek())
