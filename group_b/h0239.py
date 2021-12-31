from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):

        d = deque()
        output = []

        for ii, num in enumerate(nums[:k]): # 0,1; 1,3; 2,1
            while d and nums[d[0]] < num:   # []; [0] and 1 < 3; [1] and 3 < 1
                d.popleft()                 # []

            d.appendleft(ii)                # [2,1]

        output.append(nums[d[-1]])          # [3]
            
        for ii, num in enumerate(nums[k:], start=k): # 3,2;

            if d and d[-1] < (ii-k+1):
                d.pop()
            while d and nums[d[0]] < num:
                d.popleft()   # [1]

            d.appendleft(ii)        # 2 
            output.append(nums[d[-1]])

        return output


if __name__ == "__main__":

          #         i
          #   1
          #     _ _ _
          # 0 1 2 3 4 5
    nums = [1,3,1,2,0,5]
    k = 3
    Output = [3,3,2,5]

    # nums = [1,3,-1,-3,5,3,6,7]; k = 3
    # Output = [3,3,5,5,6,7]

    # nums = [7,2,4]
    # k = 2

    sol = Solution()
    print(sol.maxSlidingWindow(nums, k))
