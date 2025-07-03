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

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")

        # Optional: trim trailing "null"s
        while result and result[-1] == "null":
            result.pop()

        return ','.join(result)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes level-order encoded data to tree using BFS."""
        if not data:
            return None
        
        values = data.split(',')
        if values[0] == "null":
            return None
        
        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1
        
        while queue and i < len(values):
            node = queue.popleft()
            
            # Left child
            if values[i] != "null":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1
            
            # Right child
            if i < len(values) and values[i] != "null":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1
        
        return root

def inorder_tree(root):
    if not root:
        return
    
    inorder_tree(root.left)
    print(root.val, end="=>")
    inorder_tree(root.right)

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