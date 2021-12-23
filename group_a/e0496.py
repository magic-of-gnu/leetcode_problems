class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        n = len(nums2)
        
        st = []
        next_inds = [0] * n
        val2inds = dict()
        
        for ii in range(n-1, -1, -1):
            while True:
                if not st or nums2[ii] < nums2[st[-1]]:
                    break
            
                st.pop()
                
            if not st:
                next_inds[ii] = n-1
            else:
                next_inds[ii] = st[-1]
                
            val2inds[nums2[ii]] = ii
            st.append(ii)
            
        results = []
        for x in nums1:
            v = nums2[next_inds[val2inds[x]]]
            if x < v:
                results.append(v)
            else:
                results.append(-1)
        
        return results
