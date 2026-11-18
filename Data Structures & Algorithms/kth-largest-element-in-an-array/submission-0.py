class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap, k = nums, k
        heapq.heapify(minHeap)
        while len(minHeap) > k:
            heapq.heappop(minHeap)
        
        return minHeap[0]


# def __init__(self, k: int, nums: List[int]):
#         self.minHeap, self.k = nums, k
#         heapq.heapify(self.minHeap)
#         while len(self.minHeap) > k:
#             heapq.heappop(self.minHeap)

#     def add(self, val: int) -> int:
#         heapq.heappush(self.minHeap, val)
#         if (len(self.minHeap) > self.k):
#             heapq.heappop(self.minHeap)
        
#         return self.minHeap[0]
