from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:

        def is_valid(window_counter, extra_chars, char):

            res = True

            for x in 'QWER':
                if x not in extra_chars:
                    res &= True
                else: 
                    res &= window_counter.get(x, 0) >= extra_chars[x]

            # print(f'char: {char} res: {res}')
            # print(f'window_counter[char]: {window_counter.get(char, 0)} extra_chars[char]: {extra_chars.get(char, 0)}')
            # print(f'{res & (window_counter.get(char, 0) > extra_chars[char])}')

            if char in extra_chars:
                return res & (window_counter.get(char, 0) > extra_chars[char])
            return res




        counter = Counter(s)
        n = len(s)
        target =  n // 4

        extra_chars = {char: val - target for char, val in counter.items()
                       if target < val}  # q5 w8 r4 e3

        print(extra_chars)
        print(s)

        if not extra_chars:
            return 0

        left = 0
        window_length = n
        window_counter = Counter()
        for right in range(n):  # 0w  1w  7w 8q 9w 10w 11r 12w 13w
            print()
            print(f'left: {left} right: {right}')
            print(f'char: {s[right]}')
            print(f'window_counter: {window_counter}')

            if s[right] in extra_chars:
                print(f'incremented the counter')
                window_counter[s[right]] += 1 # w1 w2 w3 w4 w3->w4 w3 -> w4

            # while (s[left] not in extra_chars or window_counter[s[left]] > extra_chars[s[left]]) \

            print(f'window_counter: {window_counter}')
            while (s[left] not in extra_chars or is_valid(window_counter, extra_chars, s[left])) \
                and left <= right: # w4  w3 w4
                print(f'shirking from left; left: {left} window_counter: {window_counter}')

                if is_valid(window_counter, extra_chars, s[left]):
                    window_length = min(window_length, right-left)

                if s[left] in window_counter:
                    print(f'removing from window_counter')
                    window_counter[s[left]] -= 1 # w4 -> w3  w4 -> w3

                left += 1 # 2 6
                print(f'shirking from left; left: {left} window_counter: {window_counter}')


        return window_length
            

if __name__ == "__main__":

        #01234567890123456789
    s = "WWEQERQWQWWRWWERQWEQ" # q:5, w:8, e:4 r:3
    # s = "WEEQERQWQWWRWWERQWEQ" # q:5, w:7, e:5 r:3
    # s = "REEQERQWQWWRWWERQWEQ" # q:5, w:6, e:5 r:4
    # s = "REEQERQRQWWRWWERQWEQ" # q:5, w:5, e:5 r:5
    s = "QQQQ"
        #01234567
    # s = "WQWRQQQW"
    # s = "WWQQRRRRQRQQ"

    sol = Solution()
    print(sol.balancedString(s))
