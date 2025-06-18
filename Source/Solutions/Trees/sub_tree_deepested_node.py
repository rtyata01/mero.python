class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def subtree_with_all_deepest(root: TreeNode) -> TreeNode:
    def dfs(node):
        if not node:
            return 0, None
        
        left_depth, left_node = dfs(node.left)
        right_depth, right_node = dfs(node.right)
        
        if left_depth > right_depth:
            return (left_depth + 1, left_node)
        if right_depth > left_depth:
            return (right_depth + 1, right_node)
        else:
            return (left_depth + 1, node)
    
    return dfs(root)[1]

root  = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

subtree_root = subtree_with_all_deepest(root)
print("Subtree root value:", subtree_root.val)        