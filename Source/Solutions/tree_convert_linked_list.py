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
            
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

sol = DoublyLinkedList()
head = sol.flatten(root)

# To verify, traverse the linked list:
current = head
while current:
    print(current.val, end=" ")
    current = current.right