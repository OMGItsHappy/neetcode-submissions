# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def check(node, largestStack):
            if not node:
                return 0
            try:
                isGood = node.val >= largestStack[-1]
                largestStack.append(max(largestStack[-1], node.val))
            except IndexError:
                largestStack.append(node.val)
                isGood = True # First value, always good
            res = isGood + check(node.left, largestStack) + check(node.right, largestStack)
            largestStack.pop() # need to send this to children first
            return res

        return check(root, [])