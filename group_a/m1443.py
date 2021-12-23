# 1443. Minimum Time to Collect All Apples in a Tree

# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

class Solution:
    # def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
    def minTime(self, n, edges, hasApple):
        
        def dfs(v, paths, hasApple, current_path, result):
            children = paths.get(v, set())
            current_path.add(v)
            children = children.difference(current_path)

            if not children:
                # print('here')
                result[0] += int(hasApple[v])
                current_path.remove(v)
                return hasApple[v]

            if any([dfs(x, paths, hasApple, current_path, result) for x in children]) or hasApple[v]:
                result[0] += 1
                current_path.remove(v)
                return True

            current_path.remove(v)
            return False

        paths = {x: set() for x in range(n)}
        result = [0]

        for a,b in edges:
            paths[a].add(b)
            paths[b].add(a)

        dfs(0, paths, hasApple, set(), result)
        return max(0, 2*(result[0]-1))



if __name__ == "__main__":
    n = 7;
    edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]];
    hasApple = [False,False,True,False,False,True,False]
    Output = 6

    n = 4
    edges = [[0,2],[0,3],[1,2]]
    hasApple = [False,True,False,False]
    Output = 4

    # n = 17
    # edges = [[0,1],[1,4],[0,2],[2,7],[1,3],[9,14],[2,6],[9,13],[1,5],[9,12],[7,10],[2,8],[7,11],[2,9],[8,15],[8,16]]
    # hasApple = [True,True,False,True,True,False,True,False,False,True,True,True,False,False,True,False,False]
    # Output = 20

    # n = 5
    # edges = [[0,1],[0,2],[1,3],[0,4]]
    # hasApple = [False,False,False,True,False]
    # Output = 4

    # n = 7
    # edges = [[0,1],[1,2],[2,3],[2,4],[3,5],[0,6]]
    # hasApple = [True,False,False,False,True,False,False]
    # output = 6

    # n = 7
    # edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    # hasApple = [False,False,True,False,True,True,False]
    # Output = 8

    sol = Solution()
    print(sol.minTime(n, edges, hasApple))

