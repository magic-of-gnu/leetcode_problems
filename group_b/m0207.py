# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/

from collections import defaultdict


class Solution:
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    def canFinish(self, numCourses, prerequisites):
        r2l = defaultdict(set)
        l2r = defaultdict(set)

        r2l = dict()
        l2r = dict()

        for prer in prerequisites:
            a, b = prer
            # print()
            # print(f'a: {a} b: {b}')
            # print(f'l2r: {l2r}\nr2l: {r2l}')

            l2r[a] = l2r.get(a, set()).union(set([b]))
            l2r[a] = l2r.get(a, set()).union(l2r.get(b, set()))

            # print(f'1l2r: {l2r}\nr2l: {r2l}')

            r2l[b] = r2l.get(b, set()).union(set([a]))
            r2l[b] = r2l.get(b, set()).union(r2l.get(a, set()))

            # print(f'2l2r: {l2r}\nr2l: {r2l}')

            for val in r2l.get(a, set()):
                l2r[val] = l2r.get(val, set()).union(l2r.get(a, set()))

            # print(f'3l2r: {l2r}\nr2l: {r2l}')

            for val in l2r.get(a, set()):
                r2l[val] = r2l.get(val, set()).union(r2l.get(b, set()))

            # print(f'4l2r: {l2r}\nr2l: {r2l}')

            # if (b in l2r.get(a, set())) and (a in r2l.get(b, set())):
            if (b in l2r.get(a, set())) and (a in l2r.get(b, set())):
                return False


        return True

if __name__ == "__main__":
    numCourses = 6
    prerequisites = [[0,1],
                     [1,2],
                     [2,3],
                     [3,4],
                     [2,5],
                     [5,4],
                     [3,0]
                    ]

    numCourses = 20
    prerequisites = [[0,10],
                     [3,18],
                     [5,5],
                     [6,11],
                     [11,14],
                     [13,1],
                     [15,1],
                     [17,4]
                     ]

    numCourses = 4
    prerequisites = [[0,1],[2,3],[1,2],[3,0]]

    numCourses = 3
    prerequisites = [[1,0],[1,2],[0,1]]

    sol = Solution()
    print(sol.canFinish(numCourses, prerequisites))
