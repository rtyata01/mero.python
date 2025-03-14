class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_kth_from_end(head: ListNode, k: int) -> int:
    # Initialize two pointers
    fast = slow = head
    
    # Move fast pointer k steps ahead
    for _ in range(k):
        if fast is None:  
            return None
        fast = fast.next
    
    # Now move both slow and fast pointer until fast reaches the end
    while fast:
        slow = slow.next
        fast = fast.next
    
    return slow.value if slow else None

def create_linked_list(values):
    dummy_head = ListNode()
    current = dummy_head
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy_head.next

# Example usage
values = [1, 2, 3, 4, 5]
head = create_linked_list(values)

k = 2
result = find_kth_from_end(head, k)
print(f"The {k}th nearest element from the end is: {result}")
