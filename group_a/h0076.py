
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        def counters_agree(counter_pattern, counter_word):
            for k, v in counter_pattern.items():
                if v > counter_word[k]:
                    return False

            return True

        def get_min_window(min_window, new_window):
            print(f'min_word candidates, min_window: {min_window} new_window: {new_window}')
            if min_window is None:
                return new_window

            return min([min_window, new_window], key=len)

        m, n = len(s), len(t)

        window_start, window_length = 0, 0
        counter_pattern = Counter(t)
        counter_word = {x: 0 for x in counter_pattern.keys()}
        min_window = None

        while True:

            window_length += 1
            if window_start + window_length > m:
                break

            # increase counter
            if s[window_start+window_length-1] in counter_word:
                counter_word[s[window_start+window_length-1]] += 1


            if counters_agree(counter_pattern, counter_word):

                while True:
                    min_window = get_min_window(min_window, s[window_start:window_start+window_length])
                    if s[window_start] in counter_word:
                        counter_word[s[window_start]] -= 1

                    window_start += 1
                    window_length -= 1

                    if not counters_agree(counter_pattern, counter_word) or window_start+window_length > m:
                        break

        if min_window is None:
            return ""
        return min_window







if __name__ == '__main__':
    s = "ADOBECODEBANC"; t = "ABC"
    Output = "BANC"

    sol = Solution()
    print(sol.minWindow(s, t))

