class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sum = 0
        max_no = nums[0]
        no_of_elements = 0

        for n in nums:
            sum += n
            max_no = max(max_no, n)
            no_of_elements += 1

        return (sum - (max_no * (max_no + 1)) // 2) // (no_of_elements - max_no) 