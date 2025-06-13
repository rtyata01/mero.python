from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def pre_order_traverse(node: TreeNode):
    if not node:
        return
    
    print(node.value, end="->")
    pre_order_traverse(node.left)
    pre_order_traverse(node.right)

def tree_serialize(root: TreeNode):
    queue = deque()
    
    def pre_order_traverse(node, type = "T"):
        if not node:
            queue.append((type, "null"))
            print("null", end="->")
            return None
        
        queue.append((type, node.value))
        print(node.value, end="->")
        pre_order_traverse(node.left, "L")
        pre_order_traverse(node.right, "R")
    
    pre_order_traverse(root)
    return queue

def tree_deserialize(queue: deque):
    if not deque:
        return None
    
    type, value = queue.popleft()
    root  = TreeNode(value)
    current = root
    while queue:
        type, value = queue.popleft()
        if type == "L":
            newNode = TreeNode(value)
            current.left = newNode
            current = current.left
        elif type == "R":
            newNode = TreeNode(value)
            current.right = newNode
            current = current.right
    return root


def tree_deserialize_queue(queue: deque):
    if not deque:
        return None
    
    _, value = queue.popleft()
    
    if value == "null":
        return None

    node  = TreeNode(value)
    node.left = tree_deserialize_queue(queue)
    node.right = tree_deserialize_queue(queue)

    return node

print("\n Test ")       
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(f"\n {pre_order_traverse(root)}")
serialized_queue = tree_serialize(root) 

print("\nDeserialize Tree:")
new_root = tree_deserialize_queue(serialized_queue)
print(f"\n: {pre_order_traverse(new_root)}")

print("\n Test  ")           
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(6)
root.right = TreeNode(3)
root.right.right = TreeNode(5)
root.right.right.right = TreeNode(7)

print(f"\n {pre_order_traverse(root)}")
serialized_queue = tree_serialize(root) 

print("\nDeserialize Tree:")
new_root = tree_deserialize_queue(serialized_queue)
print(f"\n: {pre_order_traverse(new_root)}")
