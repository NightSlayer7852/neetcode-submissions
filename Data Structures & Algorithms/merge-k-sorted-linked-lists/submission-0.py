# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # def helper(lists, i, j):
    #     m =  (i + j) // 2
    #     res = []
    #     res.append(helper(i, m))
    #     res.append(helper(m + 1, j))
    #     return res
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if not lists or n == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        new_list = []
        for i in range(0, n - 1, 2):
            new_list.append(self.mergeLists(lists[i], lists[i + 1]))
        if n % 2 == 1:
            new_list.append(lists[-1])
        
        return self.mergeKLists(new_list)

    def mergeLists(self, l1, l2):
        res = ListNode()
        temp = res
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = ListNode(l1.val)
                l1 = l1.next
                temp = temp.next
            else:
                temp.next = ListNode(l2.val)
                l2 = l2.next
                temp = temp.next
                

        while l1:
            temp.next = ListNode(l1.val)
            l1 = l1.next
            temp = temp.next
        
        while l2:
            temp.next = ListNode(l2.val)
            l2 = l2.next
            temp = temp.next

        return res.next