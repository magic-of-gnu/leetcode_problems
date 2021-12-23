class Solution:
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    def canFinish(self, numCourses, prer):

        if numCourses == 1:
            return True

        def dfs(a2b, node, seen):
            print()
            print(f'node: {node} seen: {seen}')
            if node in seen:
                print('here')
                return False

            children = a2b.get(node, set())
            seen.add(node)

            # for child in children:
            while children:
                child = children.pop()
                if not dfs(a2b, child, seen):
                    return False

            if node in a2b:
                a2b.pop(node)

            return True

        seen = set()
        result = True
        a2b = dict()

        for (a, b) in prer:
            if a >= numCourses or b >= numCourses:
                # raise ValueError('course in prerequisites is out of numCourses; prer: {[a,b}} numCourses: {numCourses}')
                print('here')
                return False
            if a in a2b:
                a2b[a].add(b)
            else:
                a2b[a] = set([b])

        while True:
            if not a2b or result is False:
                break
            else:
                node = list(a2b.keys())[0]

            result = dfs(a2b, node, seen)

        return result

if __name__ == "__main__":
    numCourses = 2; prer = [[1,0],[0,1]]
    numCourses = 10;
    prer = [[0,1],
            [2,3],
            [1,4],
            [1,5],
            [3,9],
            [9,2]]

    numCouses = 5
    prer = [[1,4],[2,4],[3,1],[3,2]]
    Output = True


    sol = Solution()
    print(sol.canFinish(numCourses, prer))
