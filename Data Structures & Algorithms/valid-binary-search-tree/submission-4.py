# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root, mn, mx):
            if not root:
                return True

            if root.val <= mn or mx <= root.val:
                return False

            return ((not root.left or root.left.val < root.val) and check(root.left, mn, root.val)) and ((not root.right or root.right.val > root.val) and check(root.right, root.val, mx))

        return check(root, -1000000001, 1000000001)