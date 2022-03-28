class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        num_ways = {x:0 for x in range(target+1)}
        num_ways[0] = 1

        for curr in range(1, target+1):  # 1; 2
            for num in nums:             # 1
                num_ways[curr] += num_ways.get(curr-num,0)

        return num_ways[target]

