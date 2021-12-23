# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        n_total = 0
        curr = head
        while curr:
            curr = curr.next
            n_total += 1
            
        k = n_total - n
        if k == 0:
            return head.next
            
        curr = head
        for _ in range(k-1):
            curr = curr.next
            
        if curr.next is not None:
            curr.next = curr.next.next
            
        return head
            
