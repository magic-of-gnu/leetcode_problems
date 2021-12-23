from collections import defaultdict


class Solution:
    # def exist(self, board: List[List[str]], word: str) -> bool:
    def exist(self, board, word):

        m, n = len(board), len(board[0])

        def dfs(board, word, ii, jj, k, current_path, seen):

            if (ii,jj) in current_path:
                return False

            if k in seen.get((ii,jj), set()):
                return False

            if board[ii][jj] != word[k]:
                seen[(ii,jj)].add(k)
                return False

            if k == len(word) - 1:
                return True

            for di, dj in [(-1,0), (0,1), (1,0), (0,-1)]:
                x, y = ii + di, jj + dj

                if not(0 <= x < m and 0 <= y < n):
                    continue

                current_path.add((ii,jj))

                if dfs(board, word, x, y, k+1, current_path, seen):
                    return True

                current_path.remove((ii,jj))

            return False

        seen = defaultdict(set)

        for ii in range(m):
            for jj in range(n):
                if dfs(board, word, ii, jj, 0, set(), seen):
                    return True

        return False


if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"

    sol = Solution()
    print(sol.exist(board, word))
