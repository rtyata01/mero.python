class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class DoublyLinkedList:    
    def flatten(self, root: TreeNode) -> TreeNode:
        
        if not root:
            return None
        
        # Helper function to perform in-order traversal
        def in_order(node):
            if not node:
                return None, None
            
            # Recursively flatten the left subtree
            left_head, left_tail = in_order(node.left)
            
            # Update the current node's left pointer and right pointer
            if left_tail:
                left_tail.right = node
                node.left = left_tail
            else:
                # If there was no left subtree, this node is the new head
                left_head = node
            
            # Recursively flatten the right subtree
            right_head, right_tail = in_order(node.right)
            
            if right_head:
                right_head.left = node
                node.right = right_head
            else:
                # If there was no right subtree, this node is the new tail
                right_tail = node
            
            return left_head, right_tail
        
        head, _ = in_order(root)
        return head

def create_tree(values):
    if not values:
        return None
    
    root = TreeNode(values[0])  # The first value is the root
    queue = [root]  # This queue will help in assigning children nodes
    index = 1  # Start inserting nodes after the root
    
    while index < len(values):
        current = queue.pop(0)  # Pop the first element in the queue
        
        # Add the left child if it exists
        if index < len(values):
            current.left = TreeNode(values[index])
            queue.append(current.left)  # Append the left child to the queue
            index += 1
        
        # Add the right child if it exists
        if index < len(values):
            current.right = TreeNode(values[index])
            queue.append(current.right)  # Append the right child to the queue
            index += 1
    
    return root

def print_tree(root):
    if not root:
        return
    
    print_tree(root.left)
    print(root.val, end="->")
    print_tree(root.right)

nodes = [1, 2, 3, 4, 5, 7]
root = create_tree(nodes)
print_tree(root)

print()
sol = DoublyLinkedList()
head = sol.flatten(root)

# To verify, traverse the linked list:
current = head
while current:
    print(current.val, end="->")
    current = current.right