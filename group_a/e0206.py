# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList2(self, head: ListNode) -> ListNode:
        
        if not head:
            return head
        
        def traverse(node):
            if node.next is None:
                head = ListNode(node.val)
                parent = head
                return head, parent
            else:
                head, parent = traverse(node.next)
                
            new_node = ListNode(node.val)
            parent.next = new_node
            return head, new_node
        
        new_head, _ = traverse(head)
        return new_head
    
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        child = None
        
        while head:
            parent = ListNode(head.val)
            parent.next = child
            
            child = parent
            head = head.next
            
            
        return parent
