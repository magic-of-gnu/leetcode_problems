# 310. Minimum Height Trees

# A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.
# 
# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).
# 
# Return a list of all MHTs' root labels. You can return the answer in any order.
# 
# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

from pprint import pprint as pp
from copy import deepcopy

class Solution:
    def findMinHeightTrees(self, n, edges):

        def dfs(v, head_v, edges, current_path, results, heights):


            children = edges.get(v, set())
            current_path[v] = 1
            children = children.difference(set(current_path.keys()))

            # print(f'head_v: {head_v} v: {v} children: {children}')
            # print(results)
            # print('#############')
            # print(heights)

            if results.get(v, None):
                _res = results[v]

                # print()
                # print(f'results: {results}')
                # print(f'head_v: {head_v} v: {v}')
                # pp(results)
                # pp(_res)

                for end_v, new_path in _res.items():

                    if head_v == end_v:
                        continue

                    elif head_v not in new_path['path']:
                        results[head_v][end_v] = {
                                'path': {**current_path, **new_path['path']},
                                'height': 1 + new_path['height']
                        }
                    else: # head_v in new_path['path']
                        results[head_v][end_v] = {
                                'path': {key: value for key, value in new_path['path'].items() if key != head_v},
                                'height': new_path['height'] - 1
                        }

                    heights[head_v] = max(heights.get(head_v, 0), results[head_v][end_v]['height'])
                    # print(f'children before: {children}')
                    children = children.difference(set(new_path['path'].keys()))
                    # print(f'children after: {children}')

            if not children:
                results[head_v][v] = {
                        'path': deepcopy(current_path),
                        'height': len(current_path) - 1
                }
                heights[head_v] = max(heights.get(head_v, 0), len(current_path) - 1)
                current_path.pop(v)
                return

            for child in children:
                dfs(child, head_v, edges, current_path, results, heights)

            current_path.pop(v)
            return

        _edges = {x: set() for x in range(n)}
        results = {x: dict() for x in range(n)}
        heights = {x: 0 for x in range(n)}

        for item in edges:
            a, b = item
            _edges[a].add(b)
            _edges[b].add(a)

        to_traverse = set(range(n))
        queue = {0:1}

        while True:
            x = list(queue.keys())[0]
            queue.pop(x)
            to_traverse.remove(x)
            children = _edges[x].intersection(to_traverse)
            queue.update({child:1 for child in children})

            dfs(x, x, _edges, dict(), results, heights)

            if not to_traverse:
                break

        min_height = min(heights.values())
        # print(results)
        # print()
        # print(results[3])
        # print()
        # print(results[4])
        # print(heights)

        return [key for key, value in heights.items() if value == min_height]



if __name__ == "__main__":
    n = 4;
    edges = [[1,0],[1,2],[1,3]]

    # n = 6
    # edges = [[0,1],[0,2],[0,3],[3,4],[4,5]]

    # n = 4, edges = [[1,0],[1,2],[1,3]]

    n = 6;
    edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]

    sol = Solution()
    print(sol.findMinHeightTrees(n, edges))
