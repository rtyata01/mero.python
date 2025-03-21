class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def get_tree_edge_nodes(root):
    values = []
    def print_tree_left_edge(node):
        if not node:
            return
        
        left_node = print_tree_left_edge(node.left)
        values.append(node.val)
    
    def print_tree_right_edge(node):
        if not node:
            return
        
        if node.val != root.val:
            values.append(node.val)
        
        print_tree_right_edge(node.right)
    
    print_tree_left_edge(root)
    print_tree_right_edge(root)
    return values

# Example tree
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.left.right = TreeNode(11)
root.left.left.left = TreeNode(6)
root.left.left.left.left = TreeNode(8)
root.right = TreeNode(3)
root.right.right = TreeNode(5)
root.right.left = TreeNode(12)
root.right.right.right = TreeNode(7)

print("Tree edge nodes:", get_tree_edge_nodes(root))


# Example tree
root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.right.right = TreeNode(6)
root.right = TreeNode(3)
root.right.right = TreeNode(5)
root.right.right.right = TreeNode(7)

print("Tree edge nodes:", get_tree_edge_nodes(root))
