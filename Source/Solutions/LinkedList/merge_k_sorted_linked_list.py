# Merge k sorted linked lists and return it as one sorted linked list.

from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __repr__(self):
        return f"{self.val} -> {self.next}"
    
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]: # Optional refers None or LinkedListNode
        heap = []
        
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, id(node), node))  # insert head node from each linked list to heap.
                # id(node) in the tuple. it will prevent TypeError when pushing nodes with same value.
                
        head = ListNode()
        current = head
        
        while heap:
            val, _, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, id(node.next), node.next))
        
        return head.next
    
def create_linked_list(arr):
    head = ListNode()
    current = head
    for num in arr:
        current.next = ListNode(num)
        current = current.next
        
    return head.next

def print_linked_list(node : ListNode):
    result = []
    
    while node:
        result.append(node.val)
        node = node.next
        
    print(f"LinkedList Nodes: {result}")
    
# Time complexity: o (n log k) where n is total number of nodes, log k is cost of each heappop/heappush operation.
# Space complexity: o (k), number of nodes in heap at any time.

# This solution only works for sorted lists.
head1 = create_linked_list([-1, 2, 4, 5])
head2 = create_linked_list([1, 3, 4])
head3 = create_linked_list([2, 6])
lists = [head1, head2, head3]

# Run
solution = Solution()
merged_head = solution.mergeKLists(lists)

# Print output
print_linked_list(merged_head)

# If the list is unsorted, then 
# Sort each list first
def sort_linked_list(head: ListNode) -> ListNode:
    values = []
    while head:
        values.append(head.val)
        head = head.next
    values.sort()
    return create_linked_list(values)


# Flatten all values and sort once
def merge_unsorted_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    all_values = []
    for node in lists:
        while node:
            all_values.append(node.val)
            node = node.next
    all_values.sort()
    return create_linked_list(all_values)
