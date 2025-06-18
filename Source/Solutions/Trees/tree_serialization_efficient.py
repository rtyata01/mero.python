# Serialization: Convert a binary tree into a string so it can be stored or transmitted.
# Deserialization: Convert the string back into the original binary tree structure.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        def dfs(node):
            if node is None:
                return "null,"
            return str(node.val) + ',' + dfs(node.left) + dfs(node.right)
        
        return dfs(root)
    
    def deserialize(self, data: str) -> TreeNode: 
        """Decodes your encoded data to tree."""
        values = data.split(',')
        self.index = 0

        def dfs():
            if self.index >= len(values):
                return None
            
            value = values[self.index]
            self.index += 1
            
            if value == "null":
                return None
            
            node = TreeNode(int(value)) 
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
# Example Usage
codec = Codec()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

serialized = codec.serialize(root)
print(f"Serialized: {serialized}")
deserialize_root = codec.deserialize(serialized)
serialized = codec.serialize(deserialize_root)
print(f"Serialized Again: {serialized}")

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(6)
root.right = TreeNode(3)
root.right.right = TreeNode(5)
root.right.right.right = TreeNode(7)

serialized = codec.serialize(root)
print(f"Serialized: {serialized}")
deserialize_root = codec.deserialize(serialized)
serialized = codec.serialize(deserialize_root)
print(f"Serialized Again: {serialized}")
