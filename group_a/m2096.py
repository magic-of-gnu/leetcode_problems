# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:


        def dfs(node, startValue, destValue, start_path, dest_path):

            if node is None:
                return 0 # path, start or dest

            res_left = dfs(node.left)
            res_right = dfs(node.right)

            if isinstance(res_left, str) and isinstance(res_right, str):
                start_path.append('U')

                if res_left == 'dest':
                    dest_path.append('L')
                else:
                    dest_path.append('R')

                return 0
            elif isinstance(res_left, str):
                if res_left == 'start' and node.val == destValue:
                    start_path.append('U')
                    return 0

                elif res_left == 'start':
                    start_path.append('U')
                    return 'start'

                elif res_left == 'dest' and node.val == startValue:
                    dest_path.append("L")
                    return 0

                else:
                    dest_path.append("L")
                    return 'dest'

            elif isinstance(res_right, str):
                if res_right == 'start' and node.val == destValue:
                    start_path.append('U')
                    return 0

                elif res_right == 'start':
                    start_path.append('U')
                    return 'start'

                elif res_right == 'dest' and node.val == startValue:
                    dest_path.append("R")
                    return 0

                else:
                    dest_path.append("R")
                    return 'dest'


            if node.val == startValue:
                return 'start'
            elif node.val == destValue:
                return 'dest'







        
