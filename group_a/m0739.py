class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        n = len(temperatures)
        
        result = [0] * n
        
        for ii in range(n-1, -1, -1):
            while True:
                if not st:
                    break
                    
                if temperatures[ii] < temperatures[st[-1]]:
                    break
                
                st.pop()
                
            if st:
                result[ii] = st[-1] - ii
                
            st.append(ii)
            
        return result
