class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        n = len(prices)
        
        results = [x for x in prices]
        st = []
        
        next_inds = [0] * n
        
        for ii in range(n-1, -1, -1):
            while True:
                if not st:
                    break
                    
                if prices[ii] >= prices[st[-1]]:
                    results[ii] -= prices[st[-1]]
                    break
                    
                st.pop()
                
            if not st:
                next_inds[ii] = n - 1
            else:
                next_inds[ii] = st[-1]
                
            st.append(ii)
            
        return results
