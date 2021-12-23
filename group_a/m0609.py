"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], target_id: int) -> int:
        
        def dfs(tree, employee_id, total_importance):
            item = tree[employee_id]
            total_importance[0] += item['importance']

            for child in item['children']:
                dfs(tree, child, total_importance)

            return

        tree = dict()
        for item in employees:
            tree[item.id] = {
                "children": item.subordinates,
                "importance": item.importance,
            }

        total_importance = [0]
        dfs(tree, target_id, total_importance)

        return total_importance[0]
