class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while (left <= right):
            mid = (left+right)//2
            if (nums[mid] == target):
                return True
            elif (nums[mid] > target):
                right = mid - 1
            else:
                left = mid + 1

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        start_row = 0
        end_row = m-1

        if (matrix[0][0] > target or matrix[m-1][n-1] < target):
            return False

        while (start_row <= end_row):
            mid_row = (start_row + end_row)//2
            if (matrix[mid_row][0] <= target and matrix[mid_row][n-1] >= target):
                #  Check within this row
                val = self.search(matrix[mid_row], target)
                return val
            elif(matrix[mid_row][0] > target):
                end_row = mid_row - 1
            else: 
                start_row = mid_row + 1
        
        return False
            


