class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array = []
        count_zeros = 0
        non_zero_product = 1
        for num in nums:
            if (num == 0):
                count_zeros += 1
            else:
                non_zero_product *= num
        
        if (count_zeros >= 2):
            return [0]*len(nums)
        elif (count_zeros == 1):
            for num in nums:
                if (num != 0):
                    array.append(0)
                else: 
                    array.append(non_zero_product)
        else:
            for num in nums:
                array.append(non_zero_product//num)
        
        return array
    