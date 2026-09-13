"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        nodeMap = {None: None}

        def copy(node):
            return Node(node.val, node.next, node.random)

        newHead = copy(head)
        siblingNav = newHead
        nodeMap[head] = newHead
        navNode = head
        while navNode.next:
            navNode = navNode.next
            siblingNav.next = copy(navNode)
            nodeMap[navNode] = siblingNav.next
            siblingNav = siblingNav.next

        navNode = head
        siblingNav = newHead
        while navNode:
            siblingNav.random = nodeMap[navNode.random]
            navNode = navNode.next
            siblingNav = siblingNav.next

        return newHead