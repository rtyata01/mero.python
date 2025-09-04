# Find the smallest subtree that contains all the deepest nodes in a binary tree. 
# This subtree is rooted at the lowest common ancestor (LCA) of the deepest nodes.
# if the left and right subtree is balanced with 2 nodes each and same depth, then root will be the LCA.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def subtree_with_all_deepest(root: TreeNode) -> TreeNode:
    def dfs(node):
        if not node:
            return 0, None # depth, sub tree node.
                
        left_depth, left_sub = dfs(node.left)
        right_depth, right_sub = dfs(node.right)
        
        if left_depth > right_depth:
            return (left_depth + 1, left_sub)
        if right_depth > left_depth:
            return (right_depth + 1, right_sub)
        else:
            return (left_depth + 1, node) # or (right_depth + 1, node) as, left_depth = right_depth here.
    
    _, node = dfs(root)
    return node

root  = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

# 7 and 4 are the deepest node, so common ancestor subtree node is 2.
subtree_root = subtree_with_all_deepest(root)
print("Subtree root value:", subtree_root.val)

root  = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.left.left = TreeNode(7)
root.right = TreeNode(1)

# 7 is the deepest node, with no children.
subtree_root = subtree_with_all_deepest(root)
print("Subtree root value:", subtree_root.val)

root  = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

# common ancestor node is the root node i.e. 3.
subtree_root = subtree_with_all_deepest(root)
print("Subtree root value:", subtree_root.val)                
