 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head  # Slow pointer
        fast = head  # Fast pointer

        while fast and fast.next:  # Traverse until fast reaches the end
            slow = slow.next       # Move slow pointer one step
            fast = fast.next.next  # Move fast pointer two steps
            if slow == fast:       # If they meet, there's a cycle
                return True

        return False  # If fast reaches the end, there's no cycle