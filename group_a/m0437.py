class Solution():
    def pathSum(self, root, targetSum):

        def dfs(node, total_sum, targetSum, prefix_sum, result): # 10
            if node is None:
                return
            
            total_sum += node.val # 10
            
            result[0] += prefix_sum.get(total_sum-targetSum, 0)

            prefix_sum[total_sum] = prefix_sum.get(total_sum, 0) + 1

            dfs(node.left, total_sum, targetSum, prefix_sum, result)
            dfs(node.right, total_sum, targetSum, prefix_sum, result)

            prefix_sum[total_sum] -= 1
            if prefix_sum[total_sum] == 0:
                prefix_sum.pop(total_sum)
                    
            total_sum -= node.val

        result = [0]
        prefix_sum = {0:1}
        dfs(root, 0, targetSum, prefix_sum, result)
        return result[0]

