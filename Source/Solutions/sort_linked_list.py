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
    temp = ListNode()
    current = temp

    while left and right:
        if left.val < right.val:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next
        current.next = left or right
    
    return temp.next

# test
head = ListNode(5)
head.next = ListNode(3)
head.next.next = ListNode(2)
head.next.next.next = ListNode(6)
head.next.next.next.next = ListNode(4)

sorted_head = merge_sort(head)

while sorted_head:
    print(sorted_head.val, end="->")
    sorted_head = sorted_head.next
