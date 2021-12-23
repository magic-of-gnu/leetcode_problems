class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        st = []
        
        results = [-1] * n
        ind_max = max(range(n), key=lambda x: nums[x])
        
        for ii in reversed(range(ind_max + 1, ind_max + n + 1)):
            jj = ii % n
            
            while True:
                if not st:
                    break
                    
                if nums[jj] < nums[st[-1]]:
                    results[jj] = nums[st[-1]]
                    break
                    
                st.pop()
                
            st.append(jj)
            
        return results
