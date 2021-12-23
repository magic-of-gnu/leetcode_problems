# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import json
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        if root is None:
            return json.dumps(dict())
        
        def dfs(node, _id, s):
            if node is None:
                return
            s[_id] = node.val
            dfs(node.left, _id*2, s)
            dfs(node.right, _id*2+1, s)
            return
        
        s = dict()
        dfs(root, 1, s)
        return json.dumps(s)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        d = json.loads(data)
        
        if not d:
            return None
        
        nodes = {int(k): TreeNode(v) for k, v in d.items()}
        
        for _id in d.keys():
            _id = int(_id)
            nodes[_id].left = nodes.get(_id*2, None)
            nodes[_id].right = nodes.get(_id*2 + 1, None)
            
        return nodes[1]
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
