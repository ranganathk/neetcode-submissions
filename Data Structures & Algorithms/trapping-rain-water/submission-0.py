class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0]*n
        result = 0
        max_left = height[0]
        for i in range(n):
            max_left = max(max_left, height[i])
            left[i] = max_left
        
        right = [0]*n
        max_right = height[n-1]
        for j in range(n-1, -1, -1):
            max_right = max(max_right, height[j])
            right[j] = max_right

        for k in range(1, n-1):
            result += min(left[k], right[k]) - height[k]

        return result

        
