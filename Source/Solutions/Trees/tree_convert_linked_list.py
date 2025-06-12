class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def convert_to_linked_list(self, root: TreeNode):
        self.head = None
        self.tail = None
        
        if root is None:
            return None
        
        def traverse_tree(root: TreeNode):
            if root is None:
                return
            
            traverse_tree(root.left)
            new_node = SinglyLinkedListNode(root.val)
            
            if self.tail:
                self.tail.next = new_node  # New node is added at the end.
            else:
                self.head = new_node
                
            self.tail = new_node  # New node will be the new tail.
            
            traverse_tree(root.right)
        
        traverse_tree(root)
        return self.head
           

def print_linked_list(node: SinglyLinkedListNode):
    current = node
    while current is not None:
        print(current.data, end="=>")
        current = current.next  # Move to the next node in the list
    print()
    
def print_tree(root: TreeNode):
    if not root:
        return None
    
    print_tree(root.left)
    print(root.val, end="=>")
    print_tree(root.right)

# Example usage
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print("\nTree:")
    print_tree(root)
    
    sll = SinglyLinkedList()
    head = sll.convert_to_linked_list(root)
    
    print("\nSingly linked list:")
    print_linked_list(head)
