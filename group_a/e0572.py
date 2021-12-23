# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        
        if root is None and subRoot is None:
            return True
        
        if root is None:
            return False
        
        def dfs_search(node, subtree):
            if node is None:
                return False
            
            if foundSubtree(node, subtree):
                return True
            
            if dfs_search(node.left, subtree):
                return True
            
            if dfs_search(node.right, subtree):
                return True
            
            return False
        
        def foundSubtree(node, subtree):
            if node is None and subtree is None:
                return True
            elif node is None or subtree is None:
                return False
            
            if node.val == subtree.val:
                if foundSubtree(node.left, subtree.left) and foundSubtree(node.right, subtree.right):
                    return True
                
            return False
        
        return dfs_search(root, subRoot)
        
