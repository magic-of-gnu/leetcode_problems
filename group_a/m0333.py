# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        def dfs(node, result): # 10
            if node is None: # 1    # 8
                return None, None, 0, True

            num_nodes = 1
            res = False

            left = dfs(node.left, result) # 5 1 # 1, 1, 1 
            right = dfs(node.right, result)  # 8 #8 8 1
            
            if left[3] is False or right[3] is False:
                return left[0], right[1], 1, res
            
            if left[0] is None and right[0] is None:
                return node.val, node.val, 1, True
            
            elif left[0] is not None and right[0] is None: # no right child
                if left[0] < node.val and left[1] < node.val:
                    num_nodes = left[2] + 1
                    result[0] = max(result[0], num_nodes)
                    res = True
                    
                return left[0], node.val, num_nodes, res
            
            elif left[0] is None and right[0] is not None: # no right child
                if right[0] > node.val and right[1] > node.val:
                    num_nodes = right[2] + 1
                    result[0] = max(result[0], num_nodes)
                    res = True
                    
                return node.val, right[1], num_nodes, res    
                
            else:
                if left[0] < node.val and left[1] < node.val and \
                  node.val < right[0] and node.val < right[1]:
                    num_nodes = left[2] + right[2] + 1
                    result[0] = max(result[0], num_nodes)
                    res = True
                    
                return left[0], right[1], num_nodes, res
                        
                
        results = [1]
        dfs(root, results)  
        
        return results[0]
        
