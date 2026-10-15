# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Nav down untill you find both, then walk back until you get to a parent they both share. If one starts lower then the other then only that one should walk up
        """
        def nxt(node):
            if not node:
                return False
            if node.val > q.val and node.val > p.val:
                return nxt(node.left)
            if node.val < q.val and node.val < p.val:
                return nxt(node.right)
            return node

        return nxt(root)