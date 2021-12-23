# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def dfs(node, output):
            if node is None:
                return 0

            left = dfs(node.left, output)
            right = dfs(node.right, output)

            ind = max(left, right)

            if not (len(output) > ind):
                output.append([])

            output[ind].append(node.val)

            return ind + 1

        output = []

        dfs(root, output)

        return output

