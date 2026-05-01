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
        if not head:
            return None
        hashmap = {}
        newHead = Node(head.val)
        hashmap[head] = newHead
        temp1, temp2 = head, newHead
        
        while temp1.next:
            temp1 = temp1.next
            newNode = Node(temp1.val)
            temp2.next = newNode
            temp2 = temp2.next
            hashmap[temp1] = temp2
        temp2.next = None
        temp1, temp2 = head, newHead
        while temp1 and temp2:
            temp2.random = hashmap.get(temp1.random)
            temp1 = temp1.next
            temp2 = temp2.next

        return newHead