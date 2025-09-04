# Inverts a binary tree, also known as mirroring it.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root):
    
    def dfs(node):
        if not node:
            return None
        
        dummy = node.left
        node.left = node.right
        node.right = dummy
        
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return root

def invert_tree(root):
    if not root:
        return None
    
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

def create_bst(values):
    if not values:
        return None
    
    # Sort the values first to maintain the BST property
    values.sort()
    
    # Helper function to create a BST from a sorted list of values
    def build_bst_from_sorted_list(values):
        if not values:
            return None
        
        mid = len(values) // 2
        root = TreeNode(values[mid])
        root.left = build_bst_from_sorted_list(values[:mid])
        root.right = build_bst_from_sorted_list(values[mid+1:])
        return root
    
    return build_bst_from_sorted_list(values)

def inorder_traverse(root):
    if not root:
        return None
    
    inorder_traverse(root.left)
    print(root.val, end="=>")
    inorder_traverse(root.right)

# test    
nodes = [1, 2, 3, 4, 5, 6 , 7]
root = create_bst(nodes)

print("Original Tree:") 
inorder_traverse(root)

invert_tree(root)
print("\nInverted Tree:")
inorder_traverse(root)


root = TreeNode(1)
root.left = TreeNode(3)
root.left.left = TreeNode(5)
root.left.left.left = TreeNode(7)
print(f"\n\nOriginal Tree:") 
inorder_traverse(root)

invert_tree(root)
print("\nInverted Tree:")
inorder_traverse(root)