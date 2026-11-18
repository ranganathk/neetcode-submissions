class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, t in times:
            edges[u].append((v, t))
        
        minHeap = [(0, k)]
        visited = set()
        time = 0

        while minHeap:
            time1, node1 = heapq.heappop(minHeap)
            if node1 in visited:
                continue
            visited.add(node1)
            time = max(time, time1)

            for neigh, timeNeigh in edges[node1]:
                if not neigh in visited:
                    heapq.heappush(minHeap, (time1 + timeNeigh, neigh))
            
        
        if (len(visited) == n):
            return time
        
        return -1