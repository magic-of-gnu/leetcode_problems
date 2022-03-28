import random

class Solution:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.original_nums = [x for x in nums]
        

    def reset(self) -> List[int]:
        
        for ii in range(self.n):
            self.nums[ii] = self.original_nums[ii]
            
        return self.nums
        

    def shuffle(self) -> List[int]:
        
        for ii in reversed(range(self.n)):
            jj = random.randint(0, ii)
            tmp = self.nums[ii]
            self.nums[ii] = self.nums[jj]
            self.nums[jj] = tmp
            
        return self.nums
        
