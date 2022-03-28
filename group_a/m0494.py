from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {0:1}

        for num in nums:
            new_dp = defaultdict(int)
            for k, v in dp.items():
                new_dp[k+num]+=v
                new_dp[k-num]+=v

            dp = new_dp

        return dp[target]
        
