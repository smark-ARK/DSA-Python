from SinglyLinkedList import SinglyLinkedList

test = SinglyLinkedList()
test.insert_last(1)
test.insert_last(1)
test.insert_last(2)
test.insert_last(3)


def remove_duplicates(head: SinglyLinkedList._Node):
    curr = head
    while curr and curr.next:
        if curr.value == curr.next.value:
            curr.next = curr.next.next
        else:
            curr = curr.next


print(test)
remove_duplicates(test.head)
print(test)
