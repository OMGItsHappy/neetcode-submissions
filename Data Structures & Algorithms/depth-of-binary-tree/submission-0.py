# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        depth = 0

        while stack:
            node = stack.pop()
            if node[0]:
                depth = max(depth, node[1])
                stack.append((node[0].left, node[1] + 1))
                stack.append((node[0].right, node[1] + 1))

        return depth