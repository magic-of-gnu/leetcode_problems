# 442. Find All Duplicates in an Array

# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant extra space.

# store frequency in integer sign
# store value as abs(x)


class Solution:
    def findDuplicates(self, nums):
        n = len(nums)
        array_duplicated = []

        for x in nums:
            if nums[abs(x)-1] < 0:
                array_duplicated.append(x)
            else:
                nums[abs(x)-1] *= -1

        return array_duplicated


class Solution:
    def findDuplicates(self, nums):
        n = len(nums)
        array_duplicated = []

        for x in nums:
            if nums[(x-1)%n] > n:
                array_duplicated.append((x-1)%n + 1)
            else:
                nums[(x-1)%n] += n

        return array_duplicated


if __name__ == "__main__":

    nums = [4,3,2,7,8,2,3,8]
    answer = [2,3]

    # nums = [1, 1, 2]
    # answer = [1]

    sol = Solution()
    print(sol.findDuplicates(nums))
        
