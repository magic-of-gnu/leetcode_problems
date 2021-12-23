class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        counter_curr_subarrays = 0
        result_counter = 0
        counter_k = 0
        left, n = 0, len(nums)

        for right in range(n):

            counter_k += nums[right] % 2

            if counter_k == k:
                counter_curr_subarrays = 0
                while counter_k == k and left <= right:  
                    counter_curr_subarrays += 1 
                    counter_k -= nums[left] % 2
                    left += 1

            result_counter += counter_curr_subarrays
            
        return result_counter


if __name__ == "__main__":
    nums = [2,2,2,1,2,2,1,2,2,2,1,2,2]; k = 2
    output = 25

    sol = Solution()
    print(sol.numberOfSubarrays(nums, k))
