# Binary Tree Level Order Traversal

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_bfs(root): # Better solution, as BFS refers level order traversal.
    if not root:
        return []
    
    queue = deque([root])
    result = []
    
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: 
                queue.append(node.left)
            if node.right: 
                queue.append(node.right)
        result.append(level)
    return result

def level_order_traverse_dfs(root):  # using DFS, for level order while DFS is meant for depth first traversal.
    cache = {}
    
    def traverse_nodes(node, level):
        if not node:
            return
        
        if level not in cache:
            cache[level] = []
            
        cache[level].append(node.val)
        traverse_nodes(node.left, level + 1)
        traverse_nodes(node.right, level + 1)
    
    traverse_nodes(root, 0)
    return list(cache.values())

# Test 
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.right =TreeNode(6)
print(level_order_bfs(root)) # output [[1], [2, 3], [4, 5, 6]]
print(level_order_traverse_dfs(root)) 

root = TreeNode(1)
print(level_order_bfs(root)) # output [[1]]
print(level_order_traverse_dfs(root)) 

root = TreeNode(1, TreeNode(2, TreeNode(3)))
print(level_order_bfs(root)) # output [[1], [2], [3]]
print(level_order_traverse_dfs(root)) 

root = TreeNode(1, right=TreeNode(2, right=TreeNode(3)))
print(level_order_bfs(root)) # output [[1], [2], [3]]
print(level_order_traverse_dfs(root)) 