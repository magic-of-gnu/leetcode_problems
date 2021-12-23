class Solution:
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]

        anew, bnew = None, None
        idx_start = 0
        idx_end = len(intervals)

        a, b = newInterval
        # results = list()
        for idx, s in enumerate(intervals):
            if s[0] <= a <= s[1]:
                anew = s[0]
                break
            elif a < s[0]:
                anew = a
                break
        idx_start = idx

        for idx, s in enumerate(intervals[idx_start:], start=idx_start):
            if s[0] <= b <= s[1]:
                bnew = s[1]
                idx_end = idx+1
                break
            elif b < s[0]:
                idx_end = idx
                bnew = b
                break

        if anew is None and bnew is None:
            return intervals + [[a,b]]
        elif anew is not None and bnew is None:
            return intervals[:idx_start] + [[anew,b]]
        elif anew is not None and bnew is not None:
            return intervals[:idx_start] + [[anew, bnew]] + intervals[idx_end:]


if __name__ == "__main__":

    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]];
    newInterval = [4,8]

    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]];
    newInterval = [24,38]

    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]];
    newInterval = [0,38]

    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]];
    newInterval = [0,4]

    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]];
    newInterval = [-2,0]

    sol = Solution()
    print(sol.insert(intervals, newInterval))
