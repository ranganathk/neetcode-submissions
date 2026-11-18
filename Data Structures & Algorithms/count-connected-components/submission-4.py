class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0

        res = 0
        
        adj = { i:[] for i in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()

        def dfs(i):
            if i in visited:
                return

            visited.add(i)

            for j in adj[i]:
                dfs(j)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        
        return res