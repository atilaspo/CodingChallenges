# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # Initialize the previous node as None
        curr = head  # Start with the head of the list

        while curr:
            temp = curr.next  # Save the next node
            curr.next = prev  # Reverse the current node's pointer
            prev = curr       # Move prev to the current node
            curr = temp       # Move curr to the next node
            
        return prev