class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left_ind = 0
        right_ind = n - 1

        while (left_ind < right_ind):
            cur_sum = numbers[left_ind] + numbers[right_ind]
            if (cur_sum == target):
                return [left_ind + 1, right_ind + 1]
            elif (cur_sum < target):
                left_ind = (left_ind + right_ind)//2
            else:
                right_ind = (left_ind + right_ind)//2
            
        return [-1, -1]
            