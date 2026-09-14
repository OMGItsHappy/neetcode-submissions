# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        queue = [root]

        while queue:
            qLen = len(queue)
            lastSeen = None
            for i in range(qLen):
                node = queue.pop(0)
                if not node: continue
                lastSeen = lastSeen if node.val is None else node.val
                queue.append(node.left)
                queue.append(node.right)

            if lastSeen: res.append(lastSeen)

        return res

    