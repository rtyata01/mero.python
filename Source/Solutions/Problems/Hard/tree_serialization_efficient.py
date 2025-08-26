# Hard: Serialization: Convert a binary tree into a string so it can be stored or transmitted.
# Deserialization: Convert the string back into the original binary tree structure.
# Use DFS for both compact serialization and deserialization, results better performance and consume low memory.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class TreeCodec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        values = []

        def dfs(node):
            if not node:
                values.append("null")
                return
            
            values.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(values)
    
    def deserialize_dfs(self, data: str) -> TreeNode: 
        """Decodes your encoded data to tree."""
        if not data:
            return None
    
        def dfs() -> TreeNode:
            val = next(values)
            if val == "null":
                return None
            node = TreeNode(int(val)) 
            node.left = dfs()
            node.right = dfs()
            return node
        
        values = iter(data.strip().split(','))  # Using iter() and next() avoids self.index tracking.
        return dfs()

def inorder_tree(root):
    if not root:
        return
    
    inorder_tree(root.left)
    print(root.val, end="=>")
    inorder_tree(root.right)
    
# Time Complexity	
    # serialize() = O(n)
    # deserialize() = O(n)
# Space Complexity
    # serialize() = O(n)
    # deserialize() = O(n)
    
# Example Usage
codec = TreeCodec()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print("\nTree: ")
inorder_tree(root)
serialized = codec.serialize(root)
print(f"\nSerialized string: {serialized}")
deserialize_root = codec.deserialize_dfs(serialized)
print("DFS Deserialized Tree: ")
inorder_tree(root)


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(6)
root.right = TreeNode(3)
root.right.right = TreeNode(5)
root.right.right.right = TreeNode(7)

print("\n\nTree: ")
inorder_tree(root)
serialized = codec.serialize(root)
print(f"\nSerialized string: {serialized}")
deserialize_root = codec.deserialize_dfs(serialized)
print("DFS Deserialized Tree: ")
inorder_tree(root)

