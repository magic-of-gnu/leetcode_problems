from collections import Counter

class Solution:
    def minWindow(self, s, t):

        if s == t:
            return t

        def update_valids(w_counter, t_counter, valids, last_updated):
            if last_updated in w_counter and w_counter[last_updated] >= t_counter[last_updated]:
                    valids.add(last_updated)
            else:
                valids.discard(last_updated)

        t_counter, w_counter = Counter(t), dict()
        s_pruned = [(ind, char) for ind, char in enumerate(s) if char in t_counter]

        k = len(t_counter)
        n = len(s_pruned)
        min_len = len(s)
        result_l, result_r = None, None
        l, r = 0, 0
        l_ind, r_ind = 0, n - 1

        valids = set()
        last_updated = ''

        for l in range(n): # 0

            while r < n and len(valids) != k:
                r_ind = r

                if s_pruned[r_ind][1] in w_counter:
                    w_counter[s_pruned[r_ind][1]] += 1
                else:
                    w_counter[s_pruned[r_ind][1]] = 1

                r += 1
                update_valids(w_counter, t_counter, valids, s_pruned[r_ind][1])

            if len(valids) == k:


                if min_len >= s_pruned[r_ind][0]-s_pruned[l][0]+1:
                    min_len = s_pruned[r_ind][0]-s_pruned[l][0]+1

                    result_l = s_pruned[l][0]
                    result_r = s_pruned[r_ind][0]


            w_counter[s_pruned[l][1]] -= 1
            if w_counter[s_pruned[l][1]] == 0:
                w_counter.pop(s_pruned[l][1])

            update_valids(w_counter, t_counter, valids, s_pruned[l][1])

        if result_r is None:
            return ''
        return s[result_l:(result_r+1)]





if __name__ == "__main__":
    s = "ADOBECODEBANC"; t = "ABC"
    Output = "BANC"

    s = "cabwefgewcwaefgcf"
    t = "cae"
    output = "cwae"

    # s = "abc"
    # t = "ac"
    # output = "abc"

    sol = Solution()
    print(sol.minWindow(s, t))
