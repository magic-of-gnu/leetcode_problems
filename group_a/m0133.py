# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        def dfs(node, seen):
            if node is None:
                return
            
            if node.neighbors is None:
                new_node = Node(node.val, [])
                seen[new_node.val] = {'node': new_node, 'neighbors': []}
                return new_node

            for x in node.neighbors:
                if x.val in seen:
                    continue
                seen[x.val] = 1
                dfs(x, seen)
                
            new_node = Node(node.val, [])
            seen[node.val] = {'node': new_node, 'neighbors': [x.val for x in node.neighbors]}
            return new_node

        seen = dict()
        new_node = dfs(node, seen)
        
        for val in seen:
            d = seen[val]
            _node = d['node']
            for neighbor in d['neighbors']:
                _node.neighbors.append(seen[neighbor]['node'])
        
        return new_node
