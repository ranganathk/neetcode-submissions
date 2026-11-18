class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stk = []
        max_area = 0

        for i, ht in enumerate(heights):
            start = i
            while stk and ht < stk[-1][0]:
                h,j = stk.pop()
                w = i - j
                area = w * h
                max_area = max(max_area, area)
                start = j
            
            stk.append((ht, start))

        while stk:
            h, j = stk.pop()
            w = n - j
            area = w * h
            max_area = max(max_area, area)

        return max_area




