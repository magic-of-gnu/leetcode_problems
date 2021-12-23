# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if not head:
            return head
        
        nodes = []
        curr = head
        while curr:
            if len(nodes) > 0:
                nodes[-1].next = None
            nodes.append(curr)
            curr = curr.next
            
        n = len(nodes)
        
        ii, jj = 0, n - 1
        
        while True:
            if ii == jj:
                break
            elif jj - ii == 1:
                nodes[ii].next = nodes[jj]
                break
            else:
                nodes[ii].next = nodes[jj]
                nodes[jj].next = nodes[ii+1]
            
            ii += 1
            jj -= 1

        return nodes[0]
