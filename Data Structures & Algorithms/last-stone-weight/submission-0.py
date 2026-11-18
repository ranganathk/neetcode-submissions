class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for st in stones:
            heapq.heappush(max_heap, -st)

        while (len(max_heap) >= 2):
            y, x = -heapq.heappop(max_heap), -heapq.heappop(max_heap)

            if (y > x):
                heapq.heappush(max_heap, x-y)
        
        if (len(max_heap) == 0):
            return 0
        return -max_heap[0] 
