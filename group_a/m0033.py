class Solution:
    def search(self, nums, target: int) -> int:

        low, end = 0, len(nums) - 1

        while low <= end:
            mid  = low + (end-low) // 2
            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    low = mid + 1
            
            else:
                if nums[mid] <= target <= nums[end]:
                    low = mid + 1
                else:
                    end = mid - 1

        if nums[mid] != target:
            return -1

if __name__ == "__main__":

    nums = [4,5,6,7,0,1,2]; target = 3

    nums = [1,3]
    target = 0

    nums = [1,3]
    target = 2

    nums = [5,1,2,3,4]
    target = 1


    sol = Solution()
    print(sol.search(nums, target))
        

