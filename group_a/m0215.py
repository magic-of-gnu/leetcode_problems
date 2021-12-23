import heapq

class Solution:
    def findKthLargest(self, nums, k):
        if len(nums) == k:
            return min(nums)

        if k == 1:
            return max(nums)

        queue = []
        [heapq.heappush(queue, x) for x in nums[:k]]
        result = queue[0]

        for num in nums[k:]:
            if num > result:
                heapq.heappushpop(queue, num)
                result = queue[0]

        return queue[0]

if __name__ == '__main__':
    nums = [3,2,3,1,2,4,5,5,6]
    k = 2


    sol = Solution()
    print(sol.findKthLargest(nums, k))
