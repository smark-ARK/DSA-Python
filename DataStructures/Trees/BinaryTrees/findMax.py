from BinaryTree import test, TreeNode


def find_max(root: TreeNode):
    if not root:
        return float("-inf")
    res = root.data
    left = find_max(root.left)
    right = find_max(root.right)

    if left > res:
        res = left
    if right > res:
        res = right
    return res


print("\nmax: ", find_max(test))
