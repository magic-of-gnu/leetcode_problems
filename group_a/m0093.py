class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        def is_valid(num):
            if not num or int(num) > 255 or str(int(num)) != num:
                return False
            return True

        result = set()

        for l in range(1,4):
            num1 = s[:l]
            
            if not is_valid(num1):
                continue      
            for k in range(l+1,l+4):
                num2 = s[l:k]
                if not is_valid(num2):
                    continue
                for j in range(k+1,k+4):
                    num3 = s[k:j]
                    if not is_valid(num3):
                        continue
                    for h in range(j+1,j+4):
                        num4 = s[j:]
                        if len(num4) > 3 or not is_valid(num4):
                            continue

                        result.add(f"{num1}.{num2}.{num3}.{num4}")
                        
        return list(result)

