# Problem: Determine if a given binary tree is a valid BST.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def is_valid_bst(root):
    def validate(node, min_val=float('-inf'), max_val=float('inf')):
        if not node:
            return True
        if not (min_val < node.val < max_val):
            return False
        else:
            return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)
    
    return validate(root)
# Time Comlexity: o(n)
# Space Complexity: o (log n)   balanced tree, best case
# Space Complexity: o (n)       unbalanced tree, worst case
# Early stop.

def isValidBST(root):
    inorder_list = []

    def inorder(node):
        if not node:
            return
        inorder(node.left)
        inorder_list.append(node.val)
        inorder(node.right)

    inorder(root)

    # Check if the inorder list is strictly increasing
    for i in range(1, len(inorder_list)):
        if inorder_list[i] <= inorder_list[i - 1]:
            return False

    return True

# Time Comlexity: o(n)
# Space Complexity: o (log n)   balanced tree, best case
# Space Complexity: o (n)       unbalanced tree, worst case
# Full traversal and compare.

# Test 1 - Empty tree (valid BST)
print("Expected: True,", "Output:", is_valid_bst(None))

# Test 2 - Single node tree
root = TreeNode(1)
print("Expected: True,", "Output:", is_valid_bst(root))

# Test 3 - Valid BST with 3 nodes
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print("Expected: True,", "Output:", is_valid_bst(root))

# Test 4 - Invalid BST (left child > parent)
root = TreeNode(2)
root.left = TreeNode(3)  # left 3 is greater than parent 2.
root.right = TreeNode(4)
print("Expected: False,", "Output:", is_valid_bst(root))

# Test 5 - Valid BST
root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(7) 
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)
print("Expected: True,", "Output:", is_valid_bst(root))

# Test 6 - Valid BST with multiple levels
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print("Expected: True,", "Output:", is_valid_bst(root))

# Test 7 - Invalid BST with incorrect subtree values
root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(12) # right 12 greater than parent 5, and parent 10, but expected to be smaller than parent 10.
root.right = TreeNode(15) 
print("Expected: False,", "Output:", is_valid_bst(root))

# Test 8 - Duplicate values (violates BST rule)
root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(3)
print("Expected: False,", "Output:", is_valid_bst(root))