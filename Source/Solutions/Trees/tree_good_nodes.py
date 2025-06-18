# Find good nodes are the ones whose value is greater than or equal to the maximum value on the path from the root to that node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def find_good_nodes(root):
    cache = set()
    
    def dfs(node, max_value):
        if not node:
            return 0

        good_nodes_count = 0
        if node.val >= max_value:
            good_nodes_count += 1
            cache.add(node.val)

        max_value = max(max_value, node.val)
        good_nodes_count += dfs(node.left, max_value)
        good_nodes_count += dfs(node.right, max_value)
        return good_nodes_count
    
    good_nodes = dfs(root, root.val)
    print(f"Good Nodes Count: {good_nodes}")
    
    return cache

def pre_order_traverse(root):
    if not root:
        return None
    
    print(root.val, end="=>")
    pre_order_traverse(root.left)
    pre_order_traverse(root.right)
        
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

# test    
nodes = [1, 2, 3, 4, 5, 6, 7]
root = create_bst(nodes)
pre_order_traverse(root)
print(f"BST Find good Nodes: {find_good_nodes(root)}")

root = TreeNode(1)
root.left = TreeNode(3)
root.left.right = TreeNode(1)
root.left.left = TreeNode(5)
root.left.left.right = TreeNode(1)
root.left.left.left = TreeNode(7)
pre_order_traverse(root)
print(f"Random Find good Nodes: {find_good_nodes(root)}")