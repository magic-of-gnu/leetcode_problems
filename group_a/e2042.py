class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        st = []
        val = 0
        ind = 0
        while ind < len(s):
            if s[ind].isdigit():
                while ind < len(s) and s[ind].isdigit():
                    val = 10*val + int(s[ind])
                    ind += 1
                    
                print()
                print(st)
                print(val)
                if st:
                    if val > st[-1]:
                        print('popping')
                        st.pop()
                    else:
                        return False

                st.append(val)
                print(f'st: {st} val: {val}')
                val = 0
            ind += 1
                
        return True
                

if __name__ == "__main__":
    s = "hello world 5 x 5"

    s = "run white brave 1 13 16 laugh"

    sol = Solution()
    print(sol.areNumbersAscending(s))
