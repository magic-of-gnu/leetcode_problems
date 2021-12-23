# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        
        def dfs(node):
            if node.left is None and node.right is None:
                node.v1 = node.val
                node.v2 = 0
                return
            elif node.left is None and node.right is not None:
                dfs(node.right)
            elif node.left is not None and node.right is None:
                dfs(node.left)
            else:
                dfs(node.left)
                dfs(node.right)                
                
            node.v1 = node.val
            v2 = [0, 0, 0]
            if node.left:
                node.v1 += node.left.v2
                v2[0] += node.left.v1
                v2[1] += node.left.v1
                v2[2] += node.left.v2
            if node.right:
                node.v1 += node.right.v2
                v2[0] += node.right.v1
                v2[1] += node.right.v2
                v2[2] += node.right.v1
                
            node.v2 = max(v2)
            
        dfs(root)
        return max([root.v1, root.v2])
