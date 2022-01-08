class Solution:
    def findUnsortedSubarray(self, nums): # [2,1]
        n = len(nums)

        ind_min = None
        ind_max = None

        val_min, val_max = float('inf'), float('-inf')

        for ind, val in enumerate(nums):
            if ind + 1 < n and nums[ind] > nums[ind+1]:
                if val_max < val:
                    ind_max = ind
                    val_max = val

        if ind_max is None:
            return 0

        for ind in reversed(range(n)):
            val = nums[ind]
            if ind - 1 >= 0 and nums[ind-1] > nums[ind]:
                if val_min > val:
                    ind_min = ind
                    val_min = val

        # print()
        # print(f'ind_min: {ind_min} val_min: {val_min}')
        # print(f'ind_max: {ind_max} val_max: {val_max}')

        left = 0

        while left < n and nums[left] <= val_min:
            left += 1

        right = n - 1

        while right >= 0 and nums[right] >= val_max:
            right -= 1

        return right - left + 1 if right > left else 0


if __name__ == "__main__":
    #       0 1 2 3 4  5  6
    nums = [2,6,4,8,10,9,15]
    output = 5

    # nums = [1,2,3,4,5]
    # output = 0

    # nums = [2,1]
    # output = 2
    #       0 1 2 3 4 5  6
    # nums = [1,2,3,6,5,10,20]
    # output = 2

    #         |
    # nums = [1,3,2,2,2]
    # output = 4
    #       0 1 2 3 4 5 6
    nums = [1,2,2,2,4,3,3]
    output = 3

    # nums = [1,2,3,3,3]
    # output = 0

    #       0 1 2 3 4
    nums = [2,3,3,2,4]
    output = 3

    #       0 1 2 3 4
    nums = [1,2,4,5,3]
    output = 3

    #       0 1 2 3  4 5  6
    nums = [2,6,4,8,10,9,15]
    output = 5


    sol = Solution()
    print(sol.findUnsortedSubarray(nums))
