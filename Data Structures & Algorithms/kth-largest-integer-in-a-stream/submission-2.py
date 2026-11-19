class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        if (len(nums) == 0):
            self.arr = []
        else:
            self.arr = nums[len(nums) - k:]

    def add(self, val: int) -> int:
        new_lst = [x for x in self.arr if x < val] + [val] + [x for x in self.arr if x >= val]
        self.arr = new_lst[1:]
        return self.arr[0]

