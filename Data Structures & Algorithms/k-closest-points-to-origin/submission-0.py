class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        res = []
        for x,y in points:
            heapq.heappush(max_heap, (x*x + y*y, x, y))
        
        for _ in range(k):
            dist, x, y = heapq.heappop(max_heap)
            res.append([x, y])

        return res
# max_heap = []
#         for st in stones:
#             heapq.heappush(max_heap, -st)

#         while (len(max_heap) >= 2):
#             y, x = -heapq.heappop(max_heap), -heapq.heappop(max_heap)

#             if (y > x):
#                 heapq.heappush(max_heap, x-y)
        
#         if (len(max_heap) == 0):
#             return 0
#         return -max_heap[0] 

# users = [("Alice", 25), ("Bob", 30), ("Charlie", 25)]

# max_heap = []
# for name, age in users:
#     # Negate age for Max-Heap; name is left positive for ascending alphabetical fallback
#     heapq.heappush(max_heap, (-age, name))

# # Pop elements
# while max_heap:
#     neg_age, name = heapq.heappop(max_heap)
#     print(f"Name: {name}, Age: {-neg_age}")