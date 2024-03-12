from SinglyLinkedList import SinglyLinkedList

print("--------------------------")
test = SinglyLinkedList()
test.insert_last(1)
test.insert_last(2)
test.insert_last(4)


def insert_sorted(head: SinglyLinkedList._Node, key):
    prev = SinglyLinkedList._Node()
    curr = head
    new = SinglyLinkedList._Node(key)
    while curr and curr.value < key:
        prev = curr
        curr = curr.next
    new.next = curr
    prev.next = new
    return head


print(test)
test.head = insert_sorted(test.head, 3)
print(test)
