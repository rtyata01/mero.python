class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_tree_paths_sum(root):
    def dfs(node, current_sum):
        if not node:
            return 0
        
        current_sum = current_sum * 10 + node.val
        
        if not node.left and not node.right:
            return current_sum
        
        return dfs(node.left, current_sum) + dfs(node.right, current_sum)

    return dfs(root, 0)


from collections import deque

def sum_Nodes(root) -> int: 
    if not root:
        return 0
     
    total_sum = 0
    queue = deque([(root, root.val)])
     
    while queue:
        node, current_sum = queue.popleft()
         
        if not node.left and not node.right:
            total_sum += current_sum
        
        if node.left:
            queue.append((node.left, current_sum * 10 + node.left.val))
             
        if node.right:
            queue.append((node.right, current_sum * 10 + node.right.val))
             
    return total_sum
        
# Build the tree:
#         4
#        / \
#       9   0
#      / \
#     5   1
#          \
#           2

root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)
root.left.right.right = TreeNode(2)

# Run and print the result
# 495 + 4912 + 40 = 5447

# DFS Time Complexity = O(n)
# Space Complexity avg = O(log n), worst = o(n)
print(f"Expected output: 5447, Computed result: ", find_tree_paths_sum(root))

# BFS Time Complexity = O(n)
# Space Complexity avg = O(W) width of tree, worst = o(n)
print(f"Expected output: 5447, Computed result: ", sum_Nodes(root))
