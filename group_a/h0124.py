# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        def dfs(node):
            
            if node is None:
                return
            
            nonlocal max_sum
            
            dfs(node.left)
            dfs(node.right)
           
            
            children_values = []
            if node.left:
                children_values.append(node.left.sum_children)
            if node.right:
                children_values.append(node.right.sum_children)
                
            # max of path that passes through the node: max(node.val, node.val+node.left.max, node.val+node.right.max)
            sum_children = max([node.val] + [node.val + x for x in children_values])
            
            # path that starts at the left, and finished at the right
            sum_head = node.val + sum(children_values)
            
            max_sum = max([max_sum, sum_head, sum_children])
            node.sum_children = sum_children
            
            return
        
        max_sum = root.val
        dfs(root)
        
        return max_sum
