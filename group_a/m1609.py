from collections import deque

class Solution():

    def isEvenOddTree(self, node):   # node = 1
        
        def is_valid_node(node, prev_node, level):
            if level % 2 == 0: # even
                if node.val % 2 == 0 or not (prev_node.val < node.val):
                    return False
                
            else:   # odd
                if node.val % 2 == 1 or not (prev_node.val > node.val):
                    return False
                
            return True
        
        def append_array(node, arr):
            if node.left:
                arr.append(node.left)
            if node.right:
                arr.append(node.right)
                

        if node.val % 2 != 1:
            return False    

        level = 0
        arr = deque()
        arr.append(node)

        while arr:

            prev_node = arr.popleft()
            if prev_node.val % 2 == level:
                return False

            n = len(arr)
            append_array(prev_node, arr)

            for ii in range(n):
                node = arr.popleft()
                if not is_valid_node(node, prev_node, level):
                    return False
                
                prev_node = node
                append_array(node, arr)               

            level = (level + 1) % 2

        return True

