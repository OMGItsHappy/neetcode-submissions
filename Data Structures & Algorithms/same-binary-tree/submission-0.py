# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queuep = [p]
        queueq = [q]
        while queuep and queueq:
            pNode = queuep.pop(0)
            qNode = queueq.pop(0)
            if (not pNode and not qNode):
                continue

            if (pNode and not qNode) or (qNode and not pNode) or (pNode and qNode and pNode.val != qNode.val):
                return False
            queuep.append(pNode.left)
            queuep.append(pNode.right)
            queueq.append(qNode.left)
            queueq.append(qNode.right)

        return not queuep and not queueq

