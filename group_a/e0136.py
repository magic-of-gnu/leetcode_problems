class Solution:
    def singleNumber(self, nums):
        val = 0
        for x in nums:
            val ^= x

        return val




if __name__ == "__main__":
    nums = [2, 2, 1]
    nums = [2, 3, 1, 3, 1]

    sol = Solution()
    print(sol.singleNumber(nums))
