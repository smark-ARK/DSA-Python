class TreeNode:
    def __init__(self, data=None, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


# *Recursive
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


def insert(root: TreeNode, x):
    if not root:
        root = TreeNode(x)
        return root
    if x < root.data:
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right, x)
    return root


def search(root: TreeNode, x):
    if (not root) or x == root.data:
        return root
    if x < root.data:
        return search(root.left, x)
    else:
        return search(root.right, x)


test = TreeNode(5)
insert(test, 1)
insert(test, 2)
insert(test, 3)
insert(test, 4)


print("\n----Preorder-----")
preorder_traversal(test)
print("\n-----Inorder------")
inorder_traversal(test)
print("\n-----Postorder------")
postorder_traversal(test)
# print("\n-----Levelorder------")
# levelorder_traversal(test)
print("\n-----Search-----------")
print(search(test, 4))
