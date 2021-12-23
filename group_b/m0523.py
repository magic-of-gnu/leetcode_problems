# 523. Continuous Subarray Sum

# Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

# 17 June 2021

class Solution:
    # def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    def checkSubarraySum(self, nums, k):
        rems = {0:-1}
        s = 0

        for ii, x in enumerate(nums):
            s = (s + x) % k

            if s in rems and ii - rems.get(s) > 1:
                return True
            else:
                rems[s] = min(ii, rems.get(s, ii))


        return False


if __name__ == "__main__":
    nums = [23,2,4,6,7]; k = 6
    Output = True

    nums = [1,1,1,2,2,3,4,5]; k = 5
    Output = True

    nums = [6,3,4,5]; k = 5
    Output = False

    nums = [23,2,4,6,6]; k = 7
    Output = True

    # nums = [1,0]; k = 2
    # Output = False

    # nums = [0, 0]; k = 2
    # Output = True

    sol = Solution()
    print(sol.checkSubarraySum(nums, k))

