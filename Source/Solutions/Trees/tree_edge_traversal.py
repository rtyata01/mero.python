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
    
    def print_tree_rigth_edge(node):
        if not node:
            return
        
        if node.val != root.val:
            values.append(node.val)
        
        print_tree_rigth_edge(node.right)
    
    print_tree_left_edge(root)
    print_tree_rigth_edge(root)
    return values

# test    
# Example tree
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(6)
root.left.left.left.left = TreeNode(8)
root.right = TreeNode(3)
root.right.right = TreeNode(5)
root.right.right.right = TreeNode(7)

print("Tree edge nodes:", get_tree_edge_nodes(root))
