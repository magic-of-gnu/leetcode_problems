class Solution:
    def countMaxOrSubsets(self, nums):
        max_or = nums[0]
        for val in nums:
            max_or |= val

        print(f'max_or: {max_or}')


if __name__ == "__main__":
    nums = [3,2,1,5]
    output = 6

    sol = Solution()
    print(sol.countMaxOrSubsets(nums))
