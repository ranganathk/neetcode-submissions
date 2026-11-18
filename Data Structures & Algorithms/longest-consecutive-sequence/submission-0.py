class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        if len(nums) == 0 or len(nums) == 1:
            return len(nums) 

        nums.sort()

        counter = 1
        max_counter = 1
        
        for i in range(len(nums) - 1):
            if counter > max_counter:
                max_counter = counter
            
            if (nums[i+1] - nums[i] == 1):
                counter += 1
            elif(nums[i+1] == nums[i]):
                continue
            else:
                counter = 1
        
        if counter > max_counter:
            max_counter = counter

        return max_counter
