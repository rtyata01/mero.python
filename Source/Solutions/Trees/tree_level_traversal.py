class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_height(root):
    if not root:
        return 0
    
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    
    return max(left_height, right_height) + 1

def print_tree_level_nodes(root):
    values = []
    
    height = tree_height(root)
    print("Tree height: ", height)
    
    def traverse_level_nodes(root, level):
        if not root:
            return
        
        if level == 0:
            values.append(root.val)
                
        traverse_level_nodes(root.left, level - 1)
        traverse_level_nodes(root.right, level - 1)
    
    for i in range(height):
        values = []
        traverse_level_nodes(root, i)
        print("tree level:", i, values)
    
    return values    
    
# Example tree
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(8)
root.left.left.left.left = TreeNode(10)
root.left.left.left.left.left = TreeNode(12)
root.right = TreeNode(3)
root.right.right = TreeNode(5)
root.right.right.left = TreeNode(6)
root.right.right.right = TreeNode(7)

print_tree_level_nodes(root)
