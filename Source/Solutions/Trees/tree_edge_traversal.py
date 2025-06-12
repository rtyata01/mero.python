class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def get_tree_edge_nodes(root):
    values = []
    cache_nodes = []
    
    def print_tree_left_edge(node):
        if not node:
            return
        
        print_tree_left_edge(node.left)
        values.append(node.val)
        cache_nodes.append(node)
    
    def print_tree_right_edge(node):
        if not node:
            return
        
        if node != root:
            values.append(node.val)
            cache_nodes.append(node)
        
        print_tree_right_edge(node.right)
        
    def print_tree_bottom_edge(node):
        if not node:
            return
        
        if not node.left and not node.right and node not in cache_nodes:  # this does not enforce same node level check for bottom edge.
            values.append(node.val)
            cache_nodes.append(node)
        
        print_tree_bottom_edge(node.right)
        print_tree_bottom_edge(node.left)
    
    print_tree_left_edge(root)
    print_tree_right_edge(root)
    print_tree_bottom_edge(root)
    return values

# Example tree
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.left.right = TreeNode(9)
root.left.left.left = TreeNode(6)
root.right = TreeNode(3)
root.right.right = TreeNode(5)
root.right.left = TreeNode(8)
root.right.left.left = TreeNode(10)
root.right.right.left = TreeNode(12)
root.right.right.right = TreeNode(7)

print("Tree edge nodes:", get_tree_edge_nodes(root))


# Example tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(8)
root.left.right.right = TreeNode(9)
root.left.right.right.left = TreeNode(91)
root.left.right.right.right = TreeNode(92)
root.right.right = TreeNode(6)
root.right.right.right = TreeNode(10)

print("Tree edge nodes:", get_tree_edge_nodes(root))
