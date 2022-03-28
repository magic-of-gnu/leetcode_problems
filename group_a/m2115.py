class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        def dfs(node, graph, supplies, result, current_path, neg_result):
            if node in supplies:
                return True
            elif node in neg_result or node not in graph:
                return False
            
            if node in current_path:
                neg_result.add(node)
                return False
            
            current_path[node] = current_path.get(node,0) + 1
            
            can_be_cooked = True
            for child in graph[node]:
                can_be_cooked = can_be_cooked & (dfs(child, graph, supplies, result, current_path, neg_result))
                
            current_path[node] -= 1
            if current_path[node] == 0:
                current_path.pop(node)
                
            if can_be_cooked is True:
                supplies.add(node)
                result.add(node)
            else:
                neg_result.add(node)
                
            return can_be_cooked
        

        supplies = set(supplies)
        graph = dict()
        
        nrec = len(recipes)
        for ii in range(nrec):
            graph[recipes[ii]] = set(ingredients[ii])
            
            
        result = set()
        neg_result = set()
        current_path = dict()
        
        for rec in recipes:
            dfs(rec, graph, supplies, result, current_path, neg_result)
        
        return list(result)
        
