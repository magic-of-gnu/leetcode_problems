# 210. Course Schedule II

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# 
#     For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# 
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

class Solution:
    # def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    def findOrder(self, numCourses, prerequisites):

        if not prerequisites:
            return list(range(numCourses))

        a2b, b2a = dict(), dict()
        order = []
        queue = {x: 1 for x in range(numCourses)}
        ending = {x: 1 for x in range(numCourses)}
        counter = dict()

        for item in prerequisites:
            a, b = item
            counter[a] = 1
            counter[b] = 1
            if queue.get(a):
                queue.pop(a)

            if ending.get(b):
                ending.pop(b)

            if a2b.get(a):
                a2b[a].add(b)
            else:
                a2b[a] = set([b])

            if b2a.get(b):
                b2a[b].add(a)
            else:
                b2a[b] = set([a])

        set_queue = set(queue.keys())
        set_counter = set(counter.keys())
        set_ending = set(ending.keys())

        for k in set_queue.difference(set_counter):
            order.append(k)
            queue.pop(k)

        ending = {x:1 for x in set_ending.intersection(set_counter)}

        while True:

            if not queue:
                return []

            keys = list(queue.keys())
            k = keys[0]

            if (not a2b) and (not b2a):
                break

            if k in ending.keys():
                ending.pop(k)
                order.append(k)
                queue.pop(k)
                continue

            queue.pop(k)

            vals = b2a.pop(k)
            order.append(k)

            for val in vals:
                a2b[val].remove(k)
                if not a2b[val]:
                    queue[val] = 1
                    a2b.pop(val)

        if queue:
            for k in queue.keys():
                order.append(k)

        return order



if __name__ == "__main__":

    numCourses = 8
    pre = [[0,1],
                     [1,2],
                     [5,6],
                     [4,5],
                     [1,3],
                     [5,0],
                     [7,2],
                     [0,7]]

    numCourses = 2
    pre = [[0,1],[1,0]]

    numCourses = 3
    pre = [[1,0]]

    numCourses = 2
    pre = [[1,0]]

    numCourses = 4
    pre = [[3,0],[0,1]]

    numCourses = 10
    pre = [[5,8],[3,5],[1,9],[4,5],[0,2],[7,8],[4,9]]

    sol = Solution()
    print(sol.findOrder(numCourses, pre))

    pass
