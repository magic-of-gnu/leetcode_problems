# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, head: Optional[TreeNode]) -> bool:
        
        if head.left is None and head.right is None:
            return True

        def append_array(left, right, next_left, next_right):
            if left is not None:
                next_left.append(left.right)
                next_left.append(left.left)
                
            if right is not None:
                next_right.append(right.left)
                next_right.append(right.right)
            
        def compare(left, right):
            if left is None and right is None:
                return True
            elif (left and right is None) or (left is None and right):
                return False
            elif left.val == right.val:
                return True
            return False

        left, right = [head.left], [head.right]
        next_left, next_right = [], []
        while left and right:
            if len(left) != len(right):
                return False

            for ii in range(len(left)):
                if compare(left[ii], right[ii]):
                    append_array(left[ii], right[ii], next_left, next_right)
                else:
                    return False
                    
            left, right = next_left, next_right
            next_left, next_right = [], []

        return True

