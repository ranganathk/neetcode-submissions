class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # if not grid:
        #     return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0
        max_size = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            size = 1

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r,c = row + dr, col + dc
                    if (r in range(ROWS) and c in range(COLS) and grid[r][c] == 1 and (r, c) not in visited):
                        size += 1
                        q.append((r, c))
                        visited.add((r, c))
            
            return size

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    size = bfs(r, c)
                    max_size = max(max_size, size)
        
        return max_size