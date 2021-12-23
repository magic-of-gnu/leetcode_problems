# 1110. Delete Nodes And Return Forest
# https://leetcode.com/problems/delete-nodes-and-return-forest/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        def dfs(node, to_delete, new_head, roots):
            
            if node is None:
                return
            
            if new_head and node.val not in to_delete:
                roots.append(node)
            
            new_head = False
            if node.val in to_delete:
                new_head = True
                
            new_head_left = dfs(node.left, to_delete, new_head, roots)
            new_head_right = dfs(node.right, to_delete, new_head, roots)
            
            if new_head_left:
                node.left = None
                
            if new_head_right:
                node.right = None
                
            return new_head
            
        _to_delete = set(to_delete)
        roots = []
        
        dfs(root, _to_delete, True, roots)
        return roots
