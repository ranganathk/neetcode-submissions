class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_max = height[0]
        r_max = height[n-1]
        l = 1
        r = n-2
        result = 0
        while (l <= r):
            if (l_max < r_max):
                result += max(0, l_max - height[l])
                l_max = max(l_max, height[l])
                l += 1
            else:
                result += max(0, r_max - height[r])
                r_max = max(r_max, height[r])
                r -= 1
        
        return result

