"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        cur = head
        dummy = deepCopy = Node(0)
        hashmap = {None:None}
        i = 0
        while cur:
            hashmap[cur] = deepCopy.next = Node(cur.val)
            deepCopy = deepCopy.next
            cur = cur.next
        cur = head
        dummy = dummy.next
        while cur:
            dummy.random = hashmap[cur.random]
            cur = cur.next
            dummy = dummy.next
        
        return hashmap[head]


    