class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adj = { i:[] for i in range(n) }
        for n1, n2 in edges:
            adj[n2].append(n1)
            adj[n1].append(n2)
        
        visited = set()

        def dfs(i, prevNode):
            if i in visited:
                return False

            visited.add(i)

            for j in adj[i]:
                if j == prevNode:
                    continue
                if not dfs(j, i):
                    return False
            
            return True
        
        return dfs(0, -1) and (len(list(visited)) == n)