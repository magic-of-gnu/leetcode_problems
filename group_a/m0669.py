# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
            
        def dfs(node, low, high): # [4], 5
            if node is None:
                return None

            node.left = dfs(node.left, low, high) # node.left = 2
            node.right = dfs(node.right, low, high) # node.right = None

            if low <= node.val <= high: # 3
                return node

            else:
                if node.left:
                    return node.left
                elif node.right:
                    return node.right # 2
                return None

        return dfs(root, low, high) # [4]

