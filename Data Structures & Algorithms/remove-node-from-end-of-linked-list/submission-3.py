# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        temp = head
        while temp:
            temp = temp.next
            l += 1
        
        i = l - n
        if i == 0:
            return head.next
        temp = head
        for _ in range(i - 1):
            temp = temp.next
        temp.next = temp.next.next
        return head