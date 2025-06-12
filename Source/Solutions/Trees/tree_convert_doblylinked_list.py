class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class DoublyLinkedListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def convert_to_doubly_linked_list(self, root: TreeNode):
        self.head = None
        self.tail = None

        if not root:
            return None, None
                    
        # Helper function to perform in-order traversal
        def traverse_in_order(node):
            if not node:
                return
            
            # Recursively flatten the left subtree
            traverse_in_order(node.left)
            
            new_node = DoublyLinkedListNode(node.val)
            
            if self.tail:
                self.tail.next = new_node
                new_node.prev = self.tail
            else:
                self.head = new_node
            
            self.tail = new_node
            
            # Recursively flatten the right subtree
            traverse_in_order(node.right)
        
        traverse_in_order(root)
        return self.head, self.tail

def print_tree(root: TreeNode):
    if not root:
        return
    
    print_tree(root.left)
    print(root.val, end="->")
    print_tree(root.right)
    
def print_linked_list_from_head(head: DoublyLinkedListNode):
    current = head
    while current is not None:
        print(current.data, end="=>")
        current = current.next  # Move to the next node in the list
    print()

def print_linked_list_from_tail(tail: DoublyLinkedListNode):
    current = tail
    while current is not None:
        print(current.data, end="=>")
        current = current.prev  # Move to the next node in the list
    print()

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

    print()
    dll = DoublyLinkedList()
    head, tail = dll.convert_to_doubly_linked_list(root)
    
    print("\nDoubly linked list from head:")
    print_linked_list_from_head(head)
    
    print("\nDoubly linked list from tail:")
    print_linked_list_from_tail(tail)