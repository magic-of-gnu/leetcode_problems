#  0 1 2 3 4 5 6 7 8 9
# [2,3,1,1,4,3,2,1,1,1]

class Solution:
    def jump2(self, nums):
        
        if len(nums) == 1:
            return 0
        
        ind = 0
        n = len(nums)
        count = 0
        next_jump = 0
        
        #  0 1 2 3 4
        # [2,3,1,1,4]
        
        #  0 1 2
        # [3,2,1]

        #  0 1 2
        # [1,2,3]
        
        while ind < n: # 0
        # while next_jump < n: # 0
            # ind = 1
            njumps = nums[ind]   # 2
            next_jump = 0
            next_ind = ind + 1
            for ii in range(ind+1,ind+1+njumps):  # 2, min(3,2), ii = 1

                if ii == n - 1:
                    next_ind = n
                    break

                _next_jump = ii + nums[ii]               # 1 + 2 = 3
                if _next_jump > next_jump:   # 3 > 0
                    next_ind = ii            # 1
                    next_jump = _next_jump   # 3

            ind = next_ind  # 1
            count += 1      # 1


        return count

    def jump(self, nums):
        
        if len(nums) == 1:
            return 0
        
        n = len(nums)
        count = 0
        next_jump = 0
        _next_jump = 0
        current_max_pos = 0

        for ind in range(n-1):
            next_jump = max(next_jump, ind + nums[ind])

            if ind == current_max_pos:
                current_max_pos = next_jump
                count += 1

        return count
        
        





if __name__ == "__main__":
    nums = [1,2,3]
    output = 2

    nums = [2,3,1,1,4]
    output = 2

    # nums = [1,2,1,1,1]



    sol = Solution()
    print(sol.jump(nums))

