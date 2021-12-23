# 377. Combination Sum IV
# https://leetcode.com/problems/combination-sum-iv/

class Solution:
    def combinationSum4(self, nums, target):
        if target == 0:
            return 1

        if not nums:
            return 0

        if min(nums) > target:
            return 0

        memo = [0] * target
        memo[0] = 1

        for x in range(target):
            for num in nums:
                if x + num == target:
                    memo[0] += memo[x]

                if x + num >= target:
                    continue

                memo[x+num] += memo[x]

        return memo[0] - 1


if __name__ == "__main__":
    nums = [3,2,1]
    target = 12
    Output = 1

    # nums = [1,2,3]
    # target = 4
    # Output = 7

    nums = [9]
    target = 3

    nums = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    target = 10
    Output = 9


    sol = Solution()
    print(sol.combinationSum4(nums, target))
