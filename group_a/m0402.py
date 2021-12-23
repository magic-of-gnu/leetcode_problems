class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if k >= len(num):
            return "0"
        
        n = len(num)
        result = ""
        
        st = []
        next_inds = [0] * n
        
        for ii in range(n-1, -1, -1):
            
            while True:
                if not st:
                    break
                    
                if num[ii] > num[st[-1]]:
                    break
                    
                st.pop()
                
            if not st:
                next_inds[ii] = ii
            else:
                next_inds[ii] = st[-1]
                
            st.append(ii)            
        
        for ii, val in enumerate(next_inds):
            
            if k == 0:
                break
                
            if n - ii == k:
                ii = n
                break
            
            if ii != val and val < ii + k + 1:
                k -= 1
            else:
                if not result and  num[ii] == '0':
                    continue
                result += num[ii]
                
        for jj in range(ii, n):
            if not result and  num[jj] == '0':
                continue
                
            result += num[jj]
            
        if not result:
            return "0"
                
        return result
