# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def dfs(node, results):
            if node is None:
                return None
            
            dfs(node.left, results)
            results.append(node.val)
            dfs(node.right, results)
            
            
        results = []
        dfs(root, results)
        
        x = results[0]
        for val in results[1:]:
            if x >= val:
                return False
            
            x = val
        
        return True
