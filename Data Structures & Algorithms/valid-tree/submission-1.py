class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        q = deque([(0, -1)])
        visited.add(0)

        while q:
            node, parent = q.popleft()
            for adjacent in adj[node]:
                if adjacent == parent:
                    continue
                if adjacent in visited:
                    return False
                visited.add(adjacent)
                q.append((adjacent, node))

        return len(visited) == n