from collections import defaultdict


class Solution:
    def maxPoints(self, points):

        if len(points) == 2:
            return points

        def get_eq_params(a, b):
            if b[0] == a[0]: # vertical line
                m = None
                C = b[0]
            elif b[1] == a[1]: # horizontal line
                m = b[1]
                C = None
            else:
                m = (b[1]-a[1])/(b[0]-a[0])
                C = b[1] - m * b[0]

            return tuple([m, C])

        max_count = 2
        count = defaultdict(set)

        for ii in range(len(points)-1):
            for jj in range(ii+1, len(points)):
                params = get_eq_params(points[ii], points[jj])
                count[params].add(tuple(points[ii]))
                count[params].add(tuple(points[jj]))
                max_count = max(max_count, len(count[params]))

        print(count)
        return max_count


if __name__ == "__main__":

    points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]

    sol = Solution()
    print(sol.maxPoints(points))
