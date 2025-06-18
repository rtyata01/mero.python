# Compute the diameter of a binary tree.
# The length of the longest path between any two nodes, measured by the number of edges, not nodes.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def diameter_of_binary_tree(self, root: TreeNode) -> int:
        self.diameter = 0
        
        def depth(node):
            if not node:
                return 0  # Base case: If the node is None, its depth is 0
            
            # Recursively find the depth of left and right subtrees
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            
            # Update the diameter if the current path (left_depth + right_depth) is the longest seen
            self.diameter = max(self.diameter, left_depth + right_depth)
            
            # Return the height of the current node
            return max(left_depth, right_depth) + 1
        
        depth(root)
        return self.diameter  # This returns the diameter in terms of the number of edges

def get_tree_longest_path(root: TreeNode) -> int:
    def longest_path(node: TreeNode, max_length: int) -> int:
        if not node:
            return 0, max_length # Return both depth and current maxLength
        
        # Recursively calculate the depth of the left and right subtrees
        left_depth, max_length = longest_path(node.left, max_length)
        right_depth, max_length = longest_path(node.right, max_length)
        
        # Calculate the diameter at the current node
        max_length = max(max_length, left_depth + right_depth)
        
        # Return the height of the current node and the updated maxLength
        return max(left_depth, right_depth) + 1, max_length
    
    max_length = 0
    return longest_path(root, max_length)[1]


# Example tree
#       1
#      / \
#     2   3
#    / \     
#   4   5  
#
tree = Tree()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
# Longest path is: 4 → 2 → 1 → 3, which has 3 edges.
print(f"Expected length: 7, Computed Length: {tree.diameter_of_binary_tree(root)}")


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(6)
root.left.left.left.left = TreeNode(8)
root.left.left.left.left.left = TreeNode(10)
root.right = TreeNode(3)
root.right.right = TreeNode(5)
print(f"Expected length: 7, Computed Length: {get_tree_longest_path(root)}")


