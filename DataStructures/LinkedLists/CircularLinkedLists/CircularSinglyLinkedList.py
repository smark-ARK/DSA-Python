class CircularSinglyLinkedList:
    class _Node:
        def __init__(self, value=None, next=None) -> None:
            self.value = value
            self.next = next

    def __init__(self) -> None:
        self.last = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self) -> str:
        if self.is_empty():
            return ""
        curr = self.last.next
        res = ""
        while curr != self.last:
            res += str(curr.value) + " -> "
            curr = curr.next
        return res + str(curr.value)

    def is_empty(self):
        return self.size == 0

    def insert_first(self, x):
        new_node = self._Node(x)
        if self.is_empty():
            self.last = new_node
            self.last.next = self.last
        else:
            new_node.next = self.last.next
            self.last.next = new_node
        self.size += 1
        return x

    def insert_last(self, x):
        new_node = self._Node(x)
        if self.is_empty():
            self.last = new_node
            self.last.next = self.last
        else:
            new_node.next = self.last.next
            self.last.next = new_node
            self.last = new_node
        self.size += 1
        return x

    def delete_first(self):
        if self.is_empty():
            raise Exception("List is Already Empty")
        temp = self.last.next
        self.last.next = self.last.next.next
        self.size -= 1
        return temp.value


test = CircularSinglyLinkedList()
test.insert_first(2)
test.insert_last(3)
test.insert_first(1)
test.insert_last(4)
test.insert_last(5)
test.delete_first()

print(test)
