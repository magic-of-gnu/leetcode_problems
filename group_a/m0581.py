class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)
        st = []
        r = 0
        l = n
        
        for ii in range(n):
            while True:
                if not st:
                    break
                    
                if nums[st[-1]] > nums[ii]:
                    r = ii + 1
                    break
                    
                st.pop()
                
            st.append(ii)
            
        st = []
        
        for ii in reversed(range(n)):
            while True:
                if not st:
                    break
                    
                if nums[ii] > nums[st[-1]]:
                    l = ii
                    break
                
                st.pop()
                
            st.append(ii)

        return max(r - l, 0)
        
