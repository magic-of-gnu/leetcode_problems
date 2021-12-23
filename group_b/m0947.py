# 947. Most Stones Removed with Same Row or Column

# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

from collections import defaultdict

class Solution:
    def removeStones(self, stones):

        def get_first_item(s):
            '''Get first item from set

            Args:
                s (set): some set
            '''
            if not s:
                return None

            for el in s:
                return el

        # def dfs(rows, cols, pos, current_path, seen):
        def dfs(rows, cols, pos, current_path):
            r, c = pos

            # seen[0][r].add(c)
            # seen[1][c].add(r)

            current_path.add(pos)

            children = set([(r, x) for x in rows[r]])
            children = children.union(set([(x, c) for x in cols[c]]))
            children = children.difference(current_path)

            if not children:
                current_path.remove(pos)
                _prune(rows, cols, (r,c))
                return len(current_path)   # len = num_verticies - 1, but we removed one vertex

            # max_length = max([dfs(rows, cols, (item[0], item[1]), current_path, seen)
            max_length = max([dfs(rows, cols, (item[0], item[1]), current_path)
                for item in children])

            current_path.remove(pos)
            return max_length

        def prune(items, seen):
            '''Prune items by removing elements from seen

            Args:
                items (defaultdict(set)): {row or col: set(cols) or set(rows)}
                seen (defaultdict(set)): {row or col: set(cols) or set(rows)}
            '''
            for key, value in seen.items():
                items[key] = items[key].difference(value)
                if not items[key]:
                    items.pop(key)

        def _prune(rows, cols, pos):
            r, c = pos
            if rows.get(r):
                rows[r] = rows[r].difference(set([c]))
            if cols.get(c):
                cols[c] = cols[c].difference(set([r]))
            if not rows.get(r):
                rows.pop(r)
            if not cols.get(c):
                cols.pop(c)

        max_length = 0

        # seen = [defaultdict(set), defaultdict(set)]
        rows = defaultdict(set)
        cols = defaultdict(set)

        for (r, c) in stones:
            rows[r].add(c)
            cols[c].add(r)

        while rows and cols:

            r = get_first_item(rows)
            if r is not None:
                c = get_first_item(rows[r])
            else:
                c = get_first_item(cols)
                r = get_first_item(cols[c])

            max_length = max(max_length, dfs(rows, cols, (r, c), set()))

        return max_length



if __name__ == "__main__":
    stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    Output = 5

    stones = [[0,0],[0,1],[1,0],[1,1],[2,1],[2,2],[3,2],[3,3],[3,4],[4,3],[4,4]]


    sol = Solution()
    print(sol.removeStones(stones))
