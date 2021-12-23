class Solution:
    # def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
    def minSubArrayLen(self, target, nums):

        left, right, n = 0, 0, len(nums)  # 0, 0, 7
        min_size = float('inf')                       # 7
        current_sum = 0

        while right <= n: # 0<7

            if current_sum >= target:

                while current_sum >= target and left<=right: # 7>=7 and 6<=7
                    current_sum -= nums[left]    # 7-7=0;
                    left += 1                    # 7

                min_size = min(min_size, right-(left-1)) # 4; 4vs(5-2)=3, 3vs(7-6)=1

            if right < n:
                current_sum += nums[right]  # 3+7=10
            right += 1                  # 8

        return min_size if min_size < float('inf') else 0
