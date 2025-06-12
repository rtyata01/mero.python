class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def get_tree_level_nodes(root, level, cache_levels):
    if not root:
        return 0, cache_levels
    
    # Add the current node's value to the corresponding level
    if level not in cache_levels:
        cache_levels[level] = []
    
    cache_levels[level].append(root.val)
    
    # Recursively calculate the depth and collect levels for both left and right subtrees
    left_height, cache_levels = get_tree_level_nodes(root.left, level + 1, cache_levels)
    right_height, cache_levels = get_tree_level_nodes(root.right, level + 1, cache_levels)
    
    # The current level is the max depth of the left and right subtrees + 1 for the current node
    max_height = max(left_height, right_height) + 1
    
    return max_height, cache_levels

class Solution:
     def get_tree_nodes(self, root: TreeNode):
         self.cache = {}
         
         def traverse_nodes(node, level = 0):
            if not node:
                return 
            
            if level not in self.cache:
                self.cache[level] = []
                
            self.cache[level].append(node.val)
            traverse_nodes(node.left, level + 1)
            traverse_nodes(node.right, level + 1)
        
         _ = traverse_nodes(root)
         return self.cache

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

# Compute height and get nodes at each level
cache_levels = {}
start_level = 0
height, levels = get_tree_level_nodes(root, start_level, cache_levels)

print(f"Tree height: {height}")
for key, value in levels.items():
    print("Levels:", key, "Nodes:", value)

sol = Solution()
result = sol.get_tree_nodes(root)
print(result)