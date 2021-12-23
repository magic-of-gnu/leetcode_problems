class Solution:
    def eraseOverlapIntervals(self, intervals):

        end, count = -10**6, 0

        for s, e in sorted(intervals, key=lambda x: x[1]):
            if s >= end:
                end = e
            else:
                count += 1

        return count


if __name__ == "__main__":
    intervals = [[1,10], [2,5], [4,7], [5,11], [8,9]]

    sol = Solution()
    print(sol.eraseOverlapIntervals(intervals))

