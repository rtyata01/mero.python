# Hard: Serialization: Convert a binary tree into a string so it can be stored or transmitted.
# Deserialization: Convert the string back into the original binary tree structure.
# Use BFS for both serialization and deserialization, results better integration, debugging and scalability.
# BFS tends to produces many nulls entries during serialization, if the tree isn't complete or balanced.

from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string using BFS (level-order)."""
        if not root:
            return ""

        values = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node:
                values.append(str(node.val))
                queue.extend([node.left, node.right]) 
            else:
                values.append("null")

        # Optional: trim trailing "null"s
        while values and values[-1] == "null":
            values.pop()

        return ','.join(values)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes level-order encoded data to tree using BFS."""
        if not data:
            return None
        
        values = data.strip().split(',')
        index = 0
        if values[index] == "null":
            return None
        
        root = TreeNode(int(values[index]))
        queue = deque([root])
        index += 1
        
        while queue and index < len(values):
            node = queue.popleft()
            
            # Left child
            if values[index] != "null":
                node.left = TreeNode(int(values[index]))
                queue.append(node.left)
            index += 1
            
            # Right child
            if index < len(values) and values[index] != "null":
                node.right = TreeNode(int(values[index]))
                queue.append(node.right)
            index += 1
        
        return root

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
codec = Codec()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print("\nTree: ")
inorder_tree(root)
serialized = codec.serialize(root)
print(f"\nSerialized string: {serialized}")
deserialize_root = codec.deserialize(serialized)
print("BFS Deserialized Tree: ")
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
deserialize_root = codec.deserialize(serialized)
print("BFS Deserialized Tree: ")
inorder_tree(root)