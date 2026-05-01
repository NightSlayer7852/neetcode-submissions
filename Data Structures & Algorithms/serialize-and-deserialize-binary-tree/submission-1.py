# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("?")
        while res and res[-1] == "?":
            res.pop()
        return ",".join(res)


    # # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        data = list(map(str, data.split(",")))
        
        q = collections.deque()
        
        root = TreeNode(data[0])
        q.append(root)
        n = len(data)
        for i in range(1, len(data), 2):
            r = q.popleft()
            if i < n and data[i] != "?":
                r.left = TreeNode(data[i])
                q.append(r.left)
                
            if i + 1 < n and data[i + 1] != "?":
                r.right = TreeNode(data[i + 1])
                q.append(r.right)
        return root

