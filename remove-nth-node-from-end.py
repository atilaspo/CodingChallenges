# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # CREATE DUMMY NODE AND SLOW AND FAST POINTERS
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # MOVE FAST POINTER N + 1 TIMES
        for _ in range(n + 1):
            fast = fast.next

        # MOVE THE POINTERS
        while fast:
            slow = slow.next
            fast = fast.next

        # REASSIGN THE SLOW.NEXT LINK TO SLOW.NEXT.NEXT
        slow.next = slow.next.next

        # RETURN DUMMY.NEXT
        return dummy.next