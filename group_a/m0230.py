# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        def dfs(node, count, values, k):
            
            if node is None:
                return True
            
            if not dfs(node.left, count, value, k):
                return False
            
            if count[0] == k:
                values[0] = node.val
                return False
            
            count[0] += 1
            
            if not dfs(node.right, count, value, k):
                return False
            
            return True
        
        value = [0]
        dfs(root, [1], value, k)
        
        return value[0]
