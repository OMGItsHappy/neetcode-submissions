"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeMap = defaultdict(lambda: Node(0))
        nodeMap[None] = None
        navNode = head

        while navNode:
            nodeMap[navNode].val = navNode.val
            nodeMap[navNode].next = nodeMap[navNode.next]
            nodeMap[navNode].random = nodeMap[navNode.random]
            navNode = navNode.next

        return nodeMap[head]