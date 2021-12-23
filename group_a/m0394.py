class Solution:
    def decodeString(self, s: str) -> str:

        def get_num(s, ind):
            result = []
            is_num = False
            n = len(s)
            while s[ind].isdigit() and ind < n:
                result.append(s[ind])
                ind += 1
                is_num = True

            if is_num:
                return is_num, ind, int("".join(result))

            return is_num, ind, -1

        # 01234567
        # 3[a2[c]]
        def get_string(s, ind): # 3[a2[c]], 0;   3[a2[c]], 2;     3[a2[c]], 5

            n = len(s)
            result = []
            while ind < n: # 3[a2[c]], 0: 0; 3[a2[c]], 2: 2, 3; 3[a2[c]],5: 5, 6

                is_num, ind, count = get_num(s, ind) # True, 1, 3; 3a[2[c]],2: False, True, 4, 2;   s,5: False, 5, -1, False, 6, -1
                if is_num is True:
                    if s[ind] == "[":
                        ind += 1  # 5

                    # we got into left edge of the brackets
                    string_to_repeat, ind = get_string(s, ind)   # s, 2; 3[a2[c]],2: s, 5
                    result.append(''.join(string_to_repeat) * count)

                    if s[ind] == ']':
                        ind += 1

                elif s[ind] == "]":
                    return result, ind # [c], 7
                else:
                    result.append(s[ind]) # 3[a2[c]],2: [a]; s,5: [c]
                    ind += 1


            return result, ind

        ind = 0
        n = len(s)
        result = []
        while ind < n:
            _result, ind = get_string(s, ind) # 3[a2[c]], 0
            ind += 1

            result.append(''.join(_result))

        return ''.join(result)

            



if __name__ == "__main__":
    s = "3[a2[c]]"
    output = "accaccacc"

    s = "3[a]2[bc]"
    output = "aaabcbc"

    s = "2[2[y]pq4[2[jk]e1[f]]]ef"
    output = "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"

    sol = Solution()
    print(sol.decodeString(s))
