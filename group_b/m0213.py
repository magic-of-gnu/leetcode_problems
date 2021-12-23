# https://leetcode.com/problems/house-robber-ii/

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


class Solution:
    # def rob(self, nums: List[int]) -> int:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        elif len(nums) <= 3:
            return max(nums)

        prev2, prev1 = 0, 0
        current = 0
        n = len(nums)
        max_first = True
        
        val = nums[0]

        for ind, x in enumerate(nums[1:], start=1):
            if x > val:
                break
            else:
                val = x

        # import pdb; pdb.set_trace()

        prev2 = 0, False
        prev1 = 0, False
        vold = nums[ind], True
        vnew = 0, False
        max_first = False

        for x in range(1, n):
            ii = (ind+x)%n
            # print()
            # print(f'x: {x} ind: {ind} ii: {ii}')
            # print(f'prev2: {prev2} prev1: {prev1} vold: {vold} vnew: {vnew}')

            # max(prev2, prev1) --> prev2 is not max_first, prev1 is max_first
            if prev2[0] >= prev1[0]:
                # print('here')
                vnew = nums[ii] + prev2[0], prev2[1]
            else:
                # print('there')
                vnew = nums[ii] + prev1[0], prev1[1]

            # print('after')
            # print(f'x: {x} ind: {ind} ii: {ii}')
            # print(f'prev2: {prev2} prev1: {prev1} vold: {vold} vnew: {vnew}')

            prev2 = prev1
            prev1 = vold
            vold = vnew

        if vnew[1] is True:
            val = vnew[0] - nums[ii]
        else:
            val = vnew[0]

        return val


if __name__ == "__main__":
    nums = [9, 5, 10, 15, 8, 15]
    Output = 35

    # nums = [2,3,2]
    # Output = 3

    # nums = [1,2,1,0]
    # Output = 2

    sol = Solution()
    print(sol.rob(nums))

