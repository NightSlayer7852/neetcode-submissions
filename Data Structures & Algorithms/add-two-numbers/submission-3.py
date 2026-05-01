# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        carry = 0
        temp = head
        while l1 and l2:
            digit = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            temp.next = ListNode(digit)
            l1, l2, temp = l1.next, l2.next, temp.next
        
        while l1:
            digit = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            temp.next = ListNode(digit)
            l1, temp = l1.next, temp.next
        
        while l2:
            digit = ( l2.val + carry) % 10
            carry = ( l2.val + carry) // 10
            temp.next = ListNode(digit)
            l2, temp = l2.next, temp.next
        if carry:
            temp.next = ListNode(carry, None)
        return head.next
