class SinglyLinkedList:
    class _Node:
        def __init__(self, value, next=None) -> None:
            self.value = value
            self.next = next

    def __init__(self) -> None:
        self.head = None
        self.size = 0
