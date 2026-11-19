class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort
        self.arr = nums

    def add(self, val: int) -> int:
        self.arr = [x for x in self.arr if x < val] + [val] + [x for x in self.arr if x >= val]
        return self.arr[len(self.arr) - self.k]

