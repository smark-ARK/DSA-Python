from BinarySearchTree import TreeNode, insert


def is_valid(root: TreeNode, min=float("-inf"), max=float("inf")):
    if not root:
        return True
    if root.data < min or root.data > max:
        return False

    left = is_valid(root.left, min=min, max=root.data)
    if left:
        right = is_valid(root.right, min=root.data, max=max)
        return right

    return False


test = TreeNode(5)
# test.left = TreeNode(8)
# test.right = TreeNode(3)
insert(test, 1)
insert(test, 2)
insert(test, 3)
insert(test, 4)

print(is_valid(test))
