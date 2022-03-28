class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        st = []
        operands = set("+-*/")
        
        for tok in tokens:
            if tok in operands:  

                num2 = st.pop()  
                num1 = st.pop()  
                if tok == "+":
                    st.append(num1+num2) 
                elif tok == '-':
                    st.append(num1-num2)
                elif tok == "*":
                    st.append(num1*num2)
                elif tok == '/':
                    res = abs(num1)//abs(num2)
                    sign = 1
                    if (num1 < 0 and num2 > 0) or (num1 > 0 and num2 < 0):
                        sign = -1
                    
                    st.append(int(sign*res))
            else:
                st.append(int(tok))
                
        return st[0]
