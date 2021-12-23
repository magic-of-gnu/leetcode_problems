# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):

        q = [root]
        newq = []
        result = []

        while q or newq:

            if not q:
                q = newq
                newq = []
                result.append([node.val for node in q])

            node = q.pop()

            if node.left is not None:
                newq.append(node.left)

            if node.right is not None:
                newq.append(node.right)

        return result

