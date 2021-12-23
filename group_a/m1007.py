from collections import defaultdict

class Solution:
    def minDominoRotations(self, tops, bottoms):

        counter_tops = [0]*6
        counter_bots = [0]*6
        n = len(tops)

        s = set([1,2,3,4,5,6])

        for top, bot in zip(tops, bottoms):
            s.intersection_update(set([top, bot]))

            counter_tops[top-1] += 1
            counter_bots[bot-1] += 1

        if not s:
            return -1

        value = s.pop()

        return n - max(counter_tops[value-1], counter_bots[value-1])


if __name__ == "__main__":

    tops = [2,1,2,4,2,2]
    bottoms = [5,2,6,2,3,2]

    sol = Solution()
    print(sol.minDominoRotations(tops, bottoms))
