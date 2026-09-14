"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        seen = defaultdict(Node)
        visited = set()
        queue = [node]
        edges = []

        def copyNode(node, seen):
            neighbors = []
            for neighbor in node.neighbors:
                neighbors.append(seen[neighbor.val])
            newNode = seen[node.val]
            newNode.val = node.val
            newNode.neighbors = neighbors
            return newNode

        while queue:
            node = queue.pop(0)
            if node.val in visited: continue
            visited.add(node.val)

            edges.append(copyNode(node, seen))
            queue.extend(node.neighbors)

        return edges[0]

