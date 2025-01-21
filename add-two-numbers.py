# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a Dummy node
        dummy = ListNode()

        # Assign Dummy node to curr
        curr = dummy

        # Create a variable carry 
        carry = 0

        while l1 or l2 or carry:
            # Get the digits 
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry

            # Get the carry
            carry = total // 10

            # Assign to the next node the digit (if it's 18, only 8)
            curr.next = ListNode(total % 10)

            # Move the pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next