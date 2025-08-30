# Checks whether a binary tree is height-balanced.
# A balanced binary tree is a binary tree where, for every node, the height difference between the left and right subtrees is no more than 1.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root):
    """ Determines if a binary tree is balanced i.e. if the left and the right subtrees of every node differ in height by no more than 1. """
    def dfs(root):
        if not root:
            return True, 0  # isBalanded flag, tree height.
        
        left_balanced, left_height = dfs(root.left)
        if not left_balanced:
            return False, 0
        
        right_balanced, right_height = dfs(root.right)
        if not right_balanced:
            return False, 0
        
        if abs(left_height - right_height) > 1:
            return False, 0
        
        return True, max(left_height, right_height) + 1    
    
    is_balanced, _ = dfs(root)
    return is_balanced
    # return dfs(root)[0]
    

def is_balanced(root):
    """Check if a binary tree is height-balanced."""

    def dfs(node):
        if not node:
            return 0  # height of empty subtree = 0
        
        left = dfs(node.left)
        if left == -1:
            return -1  # left subtree not balanced

        right = dfs(node.right)
        if right == -1:
            return -1  # right subtree not balanced

        if abs(left - right) > 1:
            return -1  # current node not balanced

        return max(left, right) + 1  # return subtree height

    return dfs(root) != -1


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


def inorder_travers(root):
    if not root:
        return
    
    inorder_travers(root.left)
    print(root.val, end="=>")
    inorder_travers(root.right)

# test    
nodes = [1, 2, 3, 4, 5, 6 , 7]
root = create_bst(nodes)
inorder_travers(root)
print(f"\nIs tree balanced:", is_balanced(root))

root = TreeNode(1)
root.left = TreeNode(3)
root.left.left = TreeNode(5)
root.left.left.left = TreeNode(7)
inorder_travers(root)
print(f"\nIs tree balanced:", is_balanced(root))