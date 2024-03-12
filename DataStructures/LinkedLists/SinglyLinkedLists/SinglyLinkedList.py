class SinglyLinkedList:
    class _Node:
        def __init__(self, value=None, next=None) -> None:
            self.value = value
            self.next = next

    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self) -> str:
        curr = self.head
        res = ""
        while curr:
            res += str(curr.value) + " -> "
            curr = curr.next
        return res

    def is_empty(self):
        return self.size == 0

    def insert_first(self, x):
        new = self._Node(x)
        if self.size != 0:
            new.next = self.head
        self.head = new
        self.size += 1
        return x

    def insert_last(self, x):
        new = self._Node(x)
        if self.is_empty():
            self.head = new
            self.size += 1
            return x
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new
        self.size += 1
        return x

    def insert(self, pos: int, x):
        if pos < 1 or pos > self.size + 1:
            raise ValueError("Invalid Position!")
        new = self._Node(x)
        if pos == 1:
            new.next = self.head
            self.head = new
        else:
            prev = None
            curr = self.head
            count = 1
            while curr.next:
                if count == pos:
                    break
                prev = curr
                curr = curr.next
                count += 1
            new.next = curr
            prev.next = new
        self.size += 1
        return x

    def delete(self, pos: int):
        if self.size == 0:
            raise OverflowError
        if pos < 1 or pos > self.size:
            raise ValueError("Invalid Position!")
        if pos == 1:
            return self.delete_first()
        elif pos == self.size:
            return self.delete_last()
        else:
            prev = self.head
            count = 1
            while count < pos - 1:
                prev = prev.next
                count += 1
            temp = prev.next
            prev.next = temp.next
            self.size -= 1
            return temp.value

    def delete_first(self):
        if self.is_empty():
            raise Exception("LinkedList is already empty!")
        temp = self.head
        self.head = self.head.next
        return temp.value

    def delete_last(self):
        if self.is_empty():
            raise Exception("LinkedList is already empty!")
        prev = None
        curr = self.head
        while curr.next:
            prev = curr
            curr = curr.next
        prev.next = None
        return curr.value

    def search(self, x):
        if self.is_empty():
            raise Exception("LinkedList is empty!")
        curr = self.head
        while curr:
            if curr.value == x:
                return True
            curr = curr.next
        return False

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev
        return


sample_list = SinglyLinkedList()
sample_list.insert_last(1)
sample_list.insert_last(2)
sample_list.insert_last(3)
sample_list.insert_first(0)
sample_list.insert(2, 5)
print(len(sample_list))
print(sample_list)
sample_list.delete_first()
print(sample_list)
sample_list.delete(3)
print(sample_list)
print(sample_list.search(3))
sample_list.reverse()
print(sample_list)
