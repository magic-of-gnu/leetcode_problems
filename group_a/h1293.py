class Solution:

    def shortestPath(self, grid, k: int) -> int:

        def is_in_grid(ii,jj,m,n):
            if 0 <= ii < m and 0 <= jj < n:
                return True

            return False

        m, n = len(grid), len(grid[0])

        memo = dict() # (ii,jj): [k, num_steps]
        visited = dict()

        q = {(0,0,0): k}
        nextq = []
        result = [float('inf')]

        num_steps = 0

        while q:

            newq = dict()

            for state,k in q.items():
                ii, jj, num_steps = state[0], state[1], state[2]


                if num_steps > result[0]:
                    continue

                # prune
                if k < 0:
                    if (ii,jj) not in visited:
                        visited[(ii,jj)] = []
                    visited[(ii,jj)].append([num_steps, k])
                    continue

                if ii == m - 1 and jj == n - 1:
                    return num_steps
                    result[0] = min(result[0], num_steps)

                to_abandon = False

                if (ii,jj) in visited:
                    cons = visited[(ii,jj)]

                    for con in cons:
                        if con[0] <= num_steps and con[1] >= k:
                            to_abandon = True

                else:
                    visited[(ii,jj)] = []


                if to_abandon:
                    continue

                visited[(ii,jj)].append([num_steps,k])

                for di, dj in [(-1,0), (0,1), (1,0), (0,-1)]:
                    ni, nj = ii + di, jj + dj

                    if is_in_grid(ni,nj,m,n):
                        newq[(ni,nj, num_steps+1)] = max(newq.get((ni,nj, num_steps+1), -2), k-grid[ni][nj])

            q = newq

        return result[0] if result[0] != float('inf') else -1

