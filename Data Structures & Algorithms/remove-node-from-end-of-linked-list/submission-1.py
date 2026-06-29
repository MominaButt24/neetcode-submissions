# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if n == 1 and head.next == None:
            head = None
            return head

        temp = head
        count = 0
        while temp:
         count+=1
         temp = temp.next
        
        curr, prev = head, None
        for i in range(count - n):
         prev = curr
         curr = curr.next
        
        if prev == None:
            temp = head
            head = head.next
            temp = None
        else:
         prev.next = curr.next

        curr = None
        return head

        
