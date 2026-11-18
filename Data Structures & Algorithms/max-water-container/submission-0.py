class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l_ind = 0
        r_ind = n - 1
        result = 0

        while (l_ind < r_ind):
            water_volume = min(heights[l_ind], heights[r_ind]) * (r_ind - l_ind)
            result = max(result, water_volume)

            if (heights[l_ind] < heights[r_ind]):
                l_ind += 1
            else:
                r_ind -= 1

        return result