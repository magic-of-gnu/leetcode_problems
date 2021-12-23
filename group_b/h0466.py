class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:

        def prune_string(s1, n1, s2, n2):
            '''Prune s1 by looking at s2
            '''

            letters2 = set(s2)
            seen = set()

            ii, jj = 0, 0
            counter1 = 0
            counter2 = 0
            s = []

            for char in s1:
                if char in letters2:
                    s.append(char)
                    seen.add(char)

            return ''.join(s), letters2 == seen


        def count_s1_to_fit_s2(s1, n1, s2, n2):
            '''Count how many s1 needs to fit a single s2 till periodicty in s1 occurs
            '''

            ii, jj = 0, 0
            counter1, counter2 = 0, 0
            periods = {0: (0,0)}

            # get periodicity
            while True:

                if counter1 > n1:
                    return periods, ii, False

                if ii == len(s1):
                    counter1 += 1
                    ii = 0

                if jj == len(s2):
                    counter2 += 1

                    if ii in periods:
                        break

                    periods[ii] = counter1, counter2
                    jj = 0

                if s1[ii] == s2[jj]:
                    jj += 1

                ii += 1

            return periods, counter1, counter2, ii, True

        s1, is_ok = prune_string(s1, n1, s2, n2)

        if is_ok is False:
            # print('not OK')
            return 0

        # print(f'pruned_s1: {s1}')

        periods, counter1, counter2, s1_ind, is_ok = count_s1_to_fit_s2(s1, n1, s2, n2)

        if is_ok is False:
            return 0

        # remove count before hitting period
        # n1 -= periods[s1_ind][0] - int(s1_ind != 0)
        n1 = n1 - periods[s1_ind][0] - int(s1_ind != 0)
        print(f'n1: {n1}')
        s2_before_period = periods[s1_ind][1]

        s2_per_period = counter2 - periods[s1_ind][1]
        s1_per_period = counter1 - periods[s1_ind][0]
        nperiods = n1 // s1_per_period

        # s2_per_s1 = 
        # nperiods -= int((s1_ind != 0) and (nperiods > 1))
        # nperiods -= int(s1_ind != 0)

        n1 -= (nperiods * s1_per_period)
        # s2_after_period = 1 // per
        print(f'n1: {n1}')

        s2_total = nperiods * s2_per_period + s2_before_period

        print(periods, counter1, counter2, s1_ind)
        print(f's2before: {s2_before_period}')
        print(f's1_per_period: {s1_per_period}')
        print(f's2_per_period: {s2_per_period}')
        print(f'nperiods: {nperiods}')

        return s2_total // n2


if __name__ == "__main__":

    s1 = "acb"; n1 = 4; s2 = "ab"; n2 = 2;
    output = 2
    s1 = "a221qiwueqbba"; n1 = 9; s2 = "bbab"; n2 = 1;
    output = 4
    s1 = "aaa"; n1 = 3; s2 = "aa"; n2 = 1
    output = 4

    # s1 = "baba"; n1 = 11; s2 = "baab"; n2 = 1
    # output = 7

    # s1 = "aaa"; n1 = 20; s2 = "aaaaa"; n2 = 1
    # output = 12

    sol = Solution()
    print(sol.getMaxRepetitions(s1, n1, s2, n2))
