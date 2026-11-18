class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visited = set()
        minHeap = [[grid[0][0], 0, 0]]

        visited.add((0,0))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while minHeap:
            ht, r, c = heapq.heappop(minHeap)
            
            if (r == N - 1 and c == N - 1):
                return ht
            for dr, dc in directions:
                neiR = r + dr
                neiC = c + dc
                if (neiR < 0 or neiC < 0 or neiR >= N or neiC >= N or (neiR, neiC) in visited):
                    continue
                visited.add((neiR, neiC))
                heapq.heappush(minHeap, [max(ht, grid[neiR][neiC]), neiR, neiC])

