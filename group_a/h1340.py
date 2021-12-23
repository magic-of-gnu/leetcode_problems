

class Solution:

    def maxJumps(self, arr, d: int) -> int:

        def is_valid_jump(arr, source, dest):
            
            if not(0 <= dest < len(arr)):
                return False

            return arr[source] > arr[dest]

        def update_best_result(best_result, counts, node):
            best_result[0] = max(best_result[0], counts[node])
            return

        def dfs(arr, d, node, counts, best_result):

            if node in counts:
                update_best_result(best_result, counts, node)
                return counts[node]

            max_count = 0
            for ii in reversed(range(node - d, node)):
                if is_valid_jump(arr, node, ii):
                    max_count = max(max_count, dfs(arr, d, ii, counts, best_result))
                else:
                    break

            for ii in range(node + 1, node + 1 + d):
                if is_valid_jump(arr, node, ii):
                    max_count = max(max_count, dfs(arr, d, ii, counts, best_result))
                else:
                    break

            counts[node] = max_count + 1
            update_best_result(best_result, counts, node)

            return counts[node]

        counts = {x: 0 for x in range(len(arr))}
        counts = {}
        best_result = [0]
        for ii in range(len(arr)):
            dfs(arr, d, ii, counts, best_result)

        return best_result[0]



if __name__ == "__main__":
    arr = [6,4,14,6,8,13,9,7,10,6,12]
    d = 2

    arr = [3,3,3,3,3]
    d = 3

    # arr = [7,6,5,4,3,2,1]
    # d = 1

    # Input: arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
    # Output: 4

    sol = Solution()
    print(sol.maxJumps(arr, d))

