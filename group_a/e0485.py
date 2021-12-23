class Solution:
    def findMaxConsecutiveOnes(self, nums):

        count = 0
        max_count = 0

        for num in nums:
            if num == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0

        return max(max_count, count)
        

if __name__ == "__main__":
    nums = [1,1,0,1,1,1]
    output = 3

    sol = Solution()
    print(sol.findMaxConsecutiveOnes(nums))
