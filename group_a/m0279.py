import math
class Solution:
    def numSquares(self, n: int) -> int:

        def traverse(start_idx, current_sum, n, possible_squares, current_count, best_count):

            if current_count > best_count[0]:
                return -1

            if current_sum > n:
                return
            elif current_sum == n:
                best_count[0] = min(best_count[0], current_count)
                return -1

            for idx in range(start_idx, len(possible_squares)):
                val = traverse(idx, current_sum + possible_squares[idx], n, possible_squares, current_count + 1, best_count)
                if val == -1:
                    break

            return

        possible_squares = [x**2 for x in reversed(range(math.floor(math.sqrt(n))+1))]

        best_count = [n]
        print(f'possible_squares: {possible_squares}')

        traverse(0, 0, n, possible_squares, 0, best_count)

        return best_count[0]


if __name__ == "__main__":
    n = 12
    n = 13
    n = 36
    n = 29
    n = 39

    n = 13


    sol = Solution()
    print(sol.numSquares(n))
