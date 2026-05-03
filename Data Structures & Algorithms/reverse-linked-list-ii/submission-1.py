# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], l: int, r: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        dummy = ListNode(-1, head)

        prev_pointer, curr = dummy, head
        for i in range(l - 1):
            prev_pointer = prev_pointer.next
            curr = curr.next
        prev = None
        for i in range(r - l + 1):
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt
        
        prev_pointer.next.next = curr
        prev_pointer.next = prev
        return dummy.next