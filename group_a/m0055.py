# 55. Jump Game
# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums):
        if len(nums) == 1:
            return True

        if nums[0] == 0:
            return False
        elif nums[0] >= len(nums) - 1:
            return True

        ind = 0

        for ii, val in enumerate(reversed(nums[:-1]), start=1):
            if val >= ii - ind:
                ind = ii

        return ind == len(nums) - 1


if __name__ == "__main__":
    nums = [2,3,1,1,4]
    Output = True

    nums = [3,2,1,0,4]
    Output = False

    nums = [1,9,3,2,1,0,4]
    Output = True

    sol = Solution()
    print(sol.canJump(nums))
