class Solution:
    def arrayPairSum(self, nums):
        nums.sort()
        return sum([nums[ii] for ii in range(len(nums)) if ii % 2 == 0])


if __name__ == "__main__":
    nums = [1,4,3,2]
    output = 4

    nums = [6,2,6,5,1,2]

    sol = Solution()
    print(sol.arrayPairSum(nums))
