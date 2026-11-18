class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        
        adj = [ [] for i in range(n+1) ]

        def dfs(node, parent):
            if visited[node]:
                return True

            visited[node] = True

            for neigh in adj[node]:
                if neigh == parent:
                    continue
                if dfs(neigh, node):
                    return True
            
            return False
        
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            visited = [False]* (n + 1)

            if dfs(n1, -1):
                return [n1, n2]
        
        return []