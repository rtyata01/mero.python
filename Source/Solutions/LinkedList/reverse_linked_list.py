class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next          # Move slow pointer by 1 step
        fast = fast.next.next     # Move fast pointer by 2 steps
        if slow == fast:
            return True  # Cycle detected
    return False  # No cycle

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end="=>")
        current = current.next
    print()

# test
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None
head = node1

print("\nLinked list has cycle:")
print(has_cycle(head)) 

print("\nLinked list:")
print_linked_list(head)

reverse_head = reverse_linked_list(head)

print("\nReversed linked list:")
print_linked_list(reverse_head)


