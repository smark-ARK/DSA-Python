from SinglyLinkedList import SinglyLinkedList

print("--------------------------")
test = SinglyLinkedList()
test.insert_last(1)
test.insert_last(2)
test.insert_last(4)


def remove_key(head: SinglyLinkedList._Node, key):
    prev = SinglyLinkedList._Node()
    curr = head
    while curr and curr.value != key:
        prev = curr
        curr = curr.next
    if not curr:
        return
    prev.next = curr.next
    return curr.value


print(test)
remove_key(test.head, 2)
print(test)
