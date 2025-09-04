# Given, two nodes in BST, find the lowest common ancestor.
# BST tree, every node in left is smaller than parent, and every node on right is greater than parent.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor_efficient(root: TreeNode, first: TreeNode, second: TreeNode):
    # ensure, first <= second
    if first.val > second.val:
        first, second = second, first  # switch first and second, to make sure that first lower than second.
    
    while root:
        if root.val < first.val:
            root = root.right
        elif root.val > second.val:
            root = root.left
        else:
            return root
    
    return None

def lowest_common_ancestor_recursive(root: TreeNode, first: TreeNode, second: TreeNode):
    if first.val > second.val:
        first, second = second, first  # switch first and second, to make sure that first lower than second.
        
    def dfs(node):
        if not node:
            return None
        
        if first.val <= node.val <= second.val:
            return node
        elif node.val > second.val:
            return dfs(node.left)
        else:  # node.val < first.val
            return dfs(node.right)
     
    result = dfs(root)
    return result if result != None else TreeNode(-1)
 
#        6
#       / \
#      2   8
#     / \ / \
#    0  4 7  9
#      / \
#     3   5

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)


first = root.left.right.left # Node 3
second = root.left.right.right # Node 5 
result = lowest_common_ancestor_efficient(root, first, second)
print(f"Expected: 4, lowest common ancestor: ", result.val)

first = root.left.left # Node 0
second = root.left.right  # Node 4
result = lowest_common_ancestor_efficient(root, first, second)
print(f"Expected: 2, lowest common ancestor: ", result.val)

first = root.left.right.left # Node 3
second = root.right.right  # Node 9
result = lowest_common_ancestor_efficient(root, first, second)
print(f"Expected: 6, lowest common ancestor: ", result.val)

first = root.right.left # Node 7
second = root.right.right  # Node 9
result = lowest_common_ancestor_efficient(root, first, second)
print(f"Expected: 8, lowest common ancestor: ", result.val)

first = root.right # Node 8
second = root.right.right  # Node 9
result = lowest_common_ancestor_efficient(root, first, second)
print(f"Expected: 8, lowest common ancestor: ", result.val)