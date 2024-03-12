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
n6.next = n4
test.head = n1


def remove_loop(slow: SinglyLinkedList._Node, head: SinglyLinkedList._Node):
    temp = head
    while temp.next != slow.next:
        temp = temp.next
        slow = slow.next
    slow.next = None
    return head


def get_starting_point(slow: SinglyLinkedList._Node, head: SinglyLinkedList._Node):
    temp = head
    while temp != slow:
        temp = temp.next
        slow = slow.next
    return temp


def detect_loop(head: SinglyLinkedList._Node):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return remove_loop(slow, head)
            # return get_starting_point(slow, head)
    return None


# print(detect_loop(test.head).value)
# print(test)
detect_loop(test.head)
print(test)
