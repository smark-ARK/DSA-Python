from SinglyLinkedList import SinglyLinkedList

print("--------------------------")
test = SinglyLinkedList()

n1 = test._Node(1)
n2 = test._Node(2)
n3 = test._Node(3)
n4 = test._Node(4)
n5 = test._Node(5)
n6 = test._Node(6)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = None
test.head = n1


def detect_loop(head: SinglyLinkedList._Node):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False


print(detect_loop(test.head))
