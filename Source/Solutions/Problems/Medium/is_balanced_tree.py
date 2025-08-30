# Checks whether a binary tree is height-balanced.
# A balanced binary tree is a binary tree where, for every node, the height difference between the left and right subtrees is no more than 1.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root):
    """Check if a binary tree is height-balanced."""

    def dfs(node):
        if not node:
            return 0  # height of empty subtree = 0
        
        left = dfs(node.left)
        if left == -1:
            return -1  # left subtree not balanced

        right = dfs(node.right)
        if right == -1:
            return -1  # right subtree not balanced

        if abs(left - right) > 1:
            return -1  # current node not balanced

        return max(left, right) + 1  # return subtree height

    return dfs(root) != -1

root = TreeNode(5)
root.left = TreeNode(3)
root.left.right = TreeNode(4)
root.left.left = TreeNode(2)
root.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)
print(f"Is tree balanced:", is_balanced(root))

root = TreeNode(1)
root.left = TreeNode(3)
root.left.left = TreeNode(5)
root.left.left.left = TreeNode(7)
print(f"Is tree balanced:", is_balanced(root))

