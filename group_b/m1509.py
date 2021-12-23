import heapq


class Solution:

    def minDifference(self, nums):

        k = 3

        mins = heapq.nsmallest(k+1, nums)
        maxs = heapq.nlargest (k+1, nums)

        return min([maxs[-(ii+1)] - mins[ii] for ii in range(k+1)])


if __name__ == "__main__":
     nums = [1,5,0,10,14]
     output = 1

     # nums = [14,14,14,0,10,10,10]
     # nums = [0,0,0,0,10,10,10] # 10, 30
     # nums = [14,14,14,0,0,0,0] # 14
     # nums = [14,10,10,10,10,10,10] # 4

     # nums = [-14,-14,-14,0,10,10,10]
     # nums = [0,0,0,0,10,10,10]

     sol = Solution()
     print(sol.minDifference(nums))


