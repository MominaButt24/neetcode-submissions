# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        freq={}

        while head:
            if head in freq:
                return True
            freq[head] = True
            head = head.next
        return False