# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        
        if not lists:
            return None
        
        def finished(pointers):
            for p in pointers:
                if p is not None:
                    return False
            return True
        
        def min_pointers(pointers):
            m = None
            min_ind = None
            
            for ind, p in enumerate(pointers):
                if p is None:
                    continue
                    
                if m is None:
                    m = p.val
                    min_ind = ind
                else:
                    if m > p.val:
                        m = p.val
                        min_ind = ind


            return min_ind
        
        head = ListNode(None)
        ans = head
        pointers = lists
        
        while True:
            if finished(lists):
                return head.next
            
            min_ind = min_pointers(pointers)
            ans.next = pointers[min_ind]
            
            pointers[min_ind] = pointers[min_ind].next
            ans = ans.next
            
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        
        def mysort(lists, s, ind):
            if lists[ind] is None:
                return s
            
            v = lists[ind].val
            
            _s = s
            prev_s = _s
            for ii in range(k):
                if v < lists[_s.val].val:
                    node = ListNode(ind)

                    if ii == 0:
                        node.next = s
                        return node
                    else:
                        prev_s.next = node
                        node.next = _s
                        return s
                    
                elif _s.next is None: # maximum
                    node = ListNode(ind)
                    _s.next = node
                    return s
                
                prev_s = _s
                _s = _s.next
                    
        def pop_linked_list(s):
            ind = s.val
            s = s.next
            return s, ind
        
        def finished(lists):
            for x in lists:
                if x is not None:
                    return False
            return True
            
        
        head = ListNode(None)
        ans = head
        
        k = len(lists)
        sorted_list = sorted([ii for ii in range(k) if lists[ii]], key=lambda x: lists[x].val)
        
        s = ListNode(None)
        _s = s
        
        for x in sorted_list:
            node = ListNode(x)
            _s.next = node
            _s = _s.next
            
        s = s.next
        
        sorted_inds = s

        while True:
            if finished(lists):
                return head.next
            
            sorted_inds, popped_ind = pop_linked_list(sorted_inds)
            ans.next = lists[popped_ind]
            ans = ans.next
            lists[popped_ind] = lists[popped_ind].next
            
            if sorted_inds is None:
                ans.next = lists[popped_ind]
                return head.next
            sorted_inds = mysort(lists, sorted_inds, popped_ind)
