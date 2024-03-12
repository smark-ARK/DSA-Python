class DoublyLinkedList:
    class _Node:
        def __init__(self, value=None, next=None, previous=None) -> None:
            self.value = value
            self.next = next
            self.previous = previous

    def __init__(self) -> None:
        self.size = 0
        self.head = None
        self.tail = None

    def __str__(self) -> str:
        curr = self.head
        res = ""
        while curr:
            res += str(curr.value) + " -> "
            curr = curr.next
        return res + str(None)

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_first(self, x):
        new_node = self._Node(x)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.size += 1
        return x

    def insert_last(self, x):
        new_node = self._Node(x)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert(self, x, pos: int):
        if pos < 1 or pos > self.size + 1:
            raise Exception("Invalid Position!")
        if pos == 1:
            return self.insert_first(x)
        elif pos == self.size + 1:
            return self.insert_last(x)
        else:
            new_node = self._Node(x)
            count = 1
            curr = self.head
            while count != pos - 1:
                print(curr.value)
                curr = curr.next
                count += 1
            new_node.next = curr.next
            new_node.previous = curr
            curr.next.previous = new_node
            curr.next = new_node
            self.size += 1
            return x

    def delete_first(self):
        if self.is_empty():
            raise Exception("List is Already Empty!")
        temp = self.head
        self.head = self.head.next
        self.size -= 1
        return temp.value

    def delete_last(self):
        if self.is_empty():
            raise Exception("List is Already Empty!")
        temp = self.tail
        self.tail = self.tail.previous
        self.tail.next = None

        self.size -= 1
        return temp.value

    def delete(self, pos: int):
        if self.is_empty():
            raise Exception("List is Already Empty!")
        if pos < 1 or pos > self.size:
            raise Exception("Invalid Position!")
        if pos == 1:
            return self.delete_first()
        if pos == self.size:
            return self.delete_last()
        curr = self.head
        count = 1
        while count != pos:
            curr = curr.next
            count += 1
        curr.next.previous = curr.previous
        curr.previous.next = curr.next
        self.size -= 1
        return curr.value


test = DoublyLinkedList()
test.insert_first(1)
test.insert_last(2)
test.insert_last(4)
test.insert(3, 3)
test.insert_last(5)
test.insert_last(6)
print(test)
test.delete_first()
print(test)
test.delete_last()
print(test)
test.delete(3)
print(test)
