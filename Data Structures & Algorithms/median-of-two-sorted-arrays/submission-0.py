class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total  = len(nums1) + len(nums2)
        half = total // 2

        if (len(B) < len(A)):
            A, B = B, A
        
        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2
            a_l = A[i] if i >= 0 else float('-infinity')
            a_r = A[i+1] if (i+1) < len(A) else float("infinity")
            b_l = B[j] if j >= 0 else float('-infinity')
            b_r = B[j+1] if (j+1) < len(B) else float('infinity')

            # Partition is correct
            if ((a_l <= b_r) and (b_l <= a_r)):
                if (total % 2 == 0):
                    return (max(a_l, b_l) + min(a_r, b_r)) / 2
                else:
                    return min(a_r, b_r)
            elif (a_l > b_r): # Too many elements from A, so reduce the size of A
                r = i - 1
            else: # (b_l > a_r): # Too few elements from A, so increase the size of A
                l = i + 1
                