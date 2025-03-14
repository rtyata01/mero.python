class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# sort o(nlogn) time complexity.
def merge_sort(head):
    if not head or not head.next:
        return head
    
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # find second head
    second_half = slow.next
    # Break first half.
    slow.next = None

    left = merge_sort(head)
    right = merge_sort(second_half)

    return merge(left, right)

# merge the sorted halves
def merge(left, right):
    dummy = ListNode()
    current = dummy

    while left and right:
        if left.val < right.val:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next
        current.next = left or right # Assign the remaining nodes, which ever is longer.
    
    return dummy.next

def create_tree(values):
    dummy = ListNode()
    current = dummy
    
    for value in values:
        current.next = ListNode(value)
        current = current.next
    
    return dummy.next


# test
nodes = [5, 3, 2, 6, 4]
head = create_tree(nodes)

sorted_nodes = merge_sort(head)

while sorted_nodes:
    print(sorted_nodes.val, end="->")
    sorted_nodes = sorted_nodes.next
