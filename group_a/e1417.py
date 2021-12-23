# 1417. Reformat The String

# https://leetcode.com/problems/reformat-the-string/

# Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

# You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.
# 
# Return the reformatted string or return an empty string if it is impossible to reformat the string.


class Solution:
    def reformat(self, s: str) -> str:

        reformatted = ''

        counter_num, counter_alpha = 0, 0

        d_num = {str(x): 0 for x in range(10)}
        d_alpha = {x: 0 for x in "qwertyuiopasdfghjklzxcvbnm"}
        last_alpha = ''
        last_char = ''

        for char in s:
            if d_num.get(char) is not None:
                counter_num += 1
                d_num[char] += 1
                last_num = char

            if d_alpha.get(char) is not None:
                counter_alpha += 1
                d_alpha[char] += 1
                last_alpha = char

        if abs(counter_num - counter_alpha) > 1:
            return ""

        # remove extra char
        if counter_alpha > counter_num:
            counter_alpha -= 1
            d_alpha[last_alpha] -= 1
            reformatted = reformatted + last_alpha

        elif counter_alpha < counter_num:
            counter_num -= 1
            d_num[last_num] -= 1
            reformatted = reformatted + last_num


        while (counter_num != 0 and counter_alpha != 0):
            # print()

            keys_alpha = list(d_alpha.keys())
            keys_num = list(d_num.keys())

            # print(f'before {d_alpha}')
            # print(f'before {d_num}')

            for k_alpha in keys_alpha:
                if d_alpha.get(k_alpha) == 0:
                    d_alpha.pop(k_alpha)
                else:
                    counter_alpha -= 1
                    d_alpha[k_alpha] -= 1
                    break

            for k_num in keys_num:
                if d_num.get(k_num) == 0:
                    d_num.pop(k_num)
                else:
                    counter_num -= 1
                    d_num[k_num] -= 1
                    break

            # print(f'after {d_alpha}')
            # print(f'after {d_num}')

            # print(f'counter_alpha: {counter_alpha} counter_num: {counter_num}')
            # print(f'k_alpha: {k_alpha} k_num: {k_num}')

            reformatted = reformatted + str(k_alpha) + str(k_num)

        # print()
        # print()
        # print(f'after {d_alpha}')
        # print(f'after {d_num}')

        # print(f'counter_alpha: {counter_alpha} counter_num: {counter_num}')
        # print(f'k_alpha: {k_alpha} k_num: {k_num}')

        # print(f'reformatted: {reformatted}')
        return reformatted
        
        
if __name__ == "__main__":

    s = "aaabbb111222"
    s = ''
    s = 's12'

    s = "covid2019"

    sol = Solution()
    print(sol.reformat(s))
