class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def longest_tree_path(root: TreeNode, maxLength: int) -> int:
    if not root:
        return 0, maxLength  # Return both depth and current maxLength
    
    # Recursively calculate the depth of the left and right subtrees
    left_depth, maxLength = longest_tree_path(root.left, maxLength)
    right_depth, maxLength = longest_tree_path(root.right, maxLength)
    
    # Calculate the diameter at the current node
    maxLength = max(maxLength, left_depth + right_depth)
    
    # Return the height of the current node and the updated maxLength
    return max(left_depth, right_depth) + 1, maxLength

def get_tree_longest_path(root: TreeNode) -> int:
    maxLength = 0
    _, maxLength= longest_tree_path(root, maxLength)
    return maxLength

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

# Example tree
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(6)
root.left.left.left.left = TreeNode(8)
root.left.left.left.left.left = TreeNode(10)
root.right = TreeNode(3)
root.right.right = TreeNode(5)
print(f"Expected length: 7, Computed Length: {get_tree_longest_path(root)}")

tree = Tree()
print(f"Expected length: 7, Computed Length: {tree.diameter_of_binary_tree(root)}")

