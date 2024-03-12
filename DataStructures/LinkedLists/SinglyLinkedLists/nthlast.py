from SinglyLinkedList import SinglyLinkedList

test = SinglyLinkedList()
test.insert_last(1)
test.insert_last(2)
test.insert_last(3)


def nthlast(head: SinglyLinkedList._Node, n: int):
    curr = head
    count = 1
    while count < n:
        curr = curr.next
        count += 1
    right = curr
    left = head
    while right.next:
        left = left.next
        right = right.next
    return left.value


print(nthlast(test.head, 3))
