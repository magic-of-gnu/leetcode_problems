class Solution:
    def longestValidParentheses(self, s: str) -> int:        
        
        if s == "":
            return 0

        st = []
        result = 0
        last_valid_ind = 0
        
        for ind, char in enumerate(s): # 0,); 1,(; 2,)

            if char == "(":
                st.append(ind+1) # [1]
            elif char == ")": # 0,); 2,)
                if len(st) == 0:
                    last_valid_ind = ind + 1
                    continue
                else:
                    st.pop()
                    
                if len(st) == 0:
                    result = max(result, ind-last_valid_ind)  # 0 ? 1 -> 1
                else:
                    result = max(result, ind-st[-1])
                        

        if result != 0:
            return result + 1
        
        return result


if __name__ == "__main__":

    s = ")))))())))"
    ans = 2
    
    s = "()"
    # s = "(()"

    sol = Solution()
    print(sol.longestValidParentheses(s))
