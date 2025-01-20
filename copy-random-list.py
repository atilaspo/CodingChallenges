# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_copy = {None: None}  # Initialize a dictionary with None mapping to None

        curr = head
        # First pass: Create copies of all nodes
        while curr:
            copy = Node(curr.val)
            old_copy[curr] = copy
            curr = curr.next

        curr = head
        # Second pass: Set up next and random pointers for the copies
        while curr:
            copy = old_copy[curr]
            copy.next = old_copy[curr.next]
            copy.random = old_copy[curr.random]
            curr = curr.next

        return old_copy[head]