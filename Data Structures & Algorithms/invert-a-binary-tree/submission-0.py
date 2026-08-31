# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swapLevel(root):
            tmp = root.right
            root.right = root.left
            root.left = tmp

            if root.right:
                swapLevel(root.right)
            if root.left:
                swapLevel(root.left)

            return root


        if root:
            return swapLevel(root)
        return root

