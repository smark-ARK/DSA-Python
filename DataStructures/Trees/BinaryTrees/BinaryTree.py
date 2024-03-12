import sys


from Stack import Stack
from Queue import Queue


class TreeNode:
    def __init__(self, data=None, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


test = TreeNode(1)

test.left = TreeNode(2)
test.right = TreeNode(3)

""" #*Recursive
def preorder_traversal(root: TreeNode):
    if not root:
        return
    print(root.data, end=" ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)

def inorder_traversal(root: TreeNode):
    if not root:
        return
    inorder_traversal(root.left)
    print(root.data, end=" ")
    inorder_traversal(root.right)
def postorder_traversal(root: TreeNode):
    if not root:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data, end=" ")
 """


# *Iterative
def preorder_traversal(root: TreeNode):
    if not root:
        return
    stack = Stack()
    stack.push(root)
    while not stack.is_empty():
        temp = stack.pop()
        print(temp.data, end=" ")
        if temp.right:
            stack.push(temp.right)
        if temp.left:
            stack.push(temp.left)

    return


def inorder_traversal(root: TreeNode):
    if not root:
        return
    stack = Stack()
    temp = root
    while not stack.is_empty() or temp:
        if temp:
            stack.push(temp)
            temp = temp.left
        else:
            temp = stack.pop()
            print(temp.data, end=" ")
            temp = temp.right
    return


def postorder_traversal(root: TreeNode):
    if not root:
        return
    stack = Stack()
    current = root
    while current or not stack.is_empty():
        if current:
            stack.push(current)
            current = current.left
        else:
            temp = stack.peek().right
            if not temp:
                temp = stack.pop()
                print(temp.data, end=" ")
                while not stack.is_empty() and temp == stack.peek().right:
                    temp = stack.pop()
                    print(temp.data, end=" ")
            else:
                current = temp


def levelorder_traversal(root: TreeNode):
    queue = Queue()
    queue.enqueue(root)
    while not queue.is_empty():
        temp = queue.dequeue()
        print(temp.data, end=" ")
        if temp.left:
            queue.enqueue(temp.left)
        if temp.right:
            queue.enqueue(temp.right)

    return


print("\n----Preorder-----")
preorder_traversal(test)
print("\n-----Inorder------")
inorder_traversal(test)
print("\n-----Postorder------")
postorder_traversal(test)
print("\n-----Levelorder------")
levelorder_traversal(test)
