# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p, q = min([p, q], key=lambda x: x.val), max([p, q], key=lambda x: x.val)
        
        while True:
            if p.val <= root.val <= q.val:
                return root
            elif root.val < p.val:
                root = root.right
            elif root.val > q.val:
                root = root.left
