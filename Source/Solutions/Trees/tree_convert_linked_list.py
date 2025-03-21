class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTreeToLinkedList:
    def __init__(self):
        self.head = None
        self.prev = None

    def convert_to_linked_list(self, root):
        if root is None:
            return
        
        # Recursively traverse the left subtree
        self.convert_to_linked_list(root.left)
        
        # Process the current node
        if self.prev is not None:
            self.prev.right = root  # Link the previous node's right to the current node
        else:
            self.head = root  # If it's the first node, it becomes the head of the linked list
        
        # Update the previous node to the current node
        self.prev = root
        
        # Recursively traverse the right subtree
        self.convert_to_linked_list(root.right)

    def print_linked_list(self):
        current = self.head
        while current is not None:
            print(current.value, end=" ")
            current = current.right  # Move to the next node in the list
        print()

# Example usage
if __name__ == "__main__":
    # Create a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # Convert the tree to a linked list
    converter = BinaryTreeToLinkedList()
    converter.convert_to_linked_list(root)

    # Print the linked list
    converter.print_linked_list()
