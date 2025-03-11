class TreeNode:
    def __init__(self, value=0, left=None , right=None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def diameter_of_binary_tree(self, root: TreeNode) -> int:
        self.diameter = 0
        
        def depth(node):
            if not node:
                return 0
            
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            self.diameter = max(self.diameter, left_depth + right_depth)
            return max(left_depth, right_depth) + 1
        
        depth(root)
        return self.diameter
            

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(5)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(6)
root.left.left.left.left = TreeNode(8)

tree = Tree()
print(f"Expected lenght: 5, Computed Length: ", tree.diameter_of_binary_tree(root)) 