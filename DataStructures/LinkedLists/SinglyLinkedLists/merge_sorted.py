from SinglyLinkedList import SinglyLinkedList

test1 = SinglyLinkedList()
test1.insert_last(1)
test1.insert_last(3)
test1.insert_last(5)
test1.insert_last(7)

test2 = SinglyLinkedList()
test2.insert_last(2)
test2.insert_last(4)
test2.insert_last(6)


def merge_sorted(head1: SinglyLinkedList._Node, head2: SinglyLinkedList._Node):
    sentinal = SinglyLinkedList._Node()
    temp = sentinal
    p1 = head1
    p2 = head2
    while p1 and p2:
        if p1.value <= p2.value:
            temp.next = p1
            p1 = p1.next
        else:
            temp.next = p2
            p2 = p2.next
        temp = temp.next
    if p1:
        temp.next = p1
    if p2:
        temp.next = p2
    return sentinal.next


merged = merge_sorted(test1.head, test2.head)
res = ""
while merged:
    res += str(merged.value) + " -> "
    merged = merged.next
print(res)
