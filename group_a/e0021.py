# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(None)
        ans = head
        
        while True:
            
            if l1 is None:
                ans.next = l2
                return head.next
            elif l2 is None:
                ans.next = l1
                return head.next
            
            if l1.val > l2.val:
                ans.next = l2
                l2 = l2.next
            elif l1.val <= l2.val:
                ans.next = l1
                l1 = l1.next
                
            ans = ans.next
