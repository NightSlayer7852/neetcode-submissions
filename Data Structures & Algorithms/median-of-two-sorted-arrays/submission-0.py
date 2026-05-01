class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        n = len(A)
        m = len(B)
        total = n + m
        half = total // 2
        l, r = 0, n - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >=0 else float("-infinity")
            Aright = A[i + 1] if i + 1 < n else float("infinity")
            Bleft = B[j] if j >=0 else float("-infinity")
            Bright = B[j + 1] if j + 1 < m else float("infinity")

            if Aleft > Bright:
                r = i - 1
            elif Bleft > Aright:
                l = i + 1
            else:
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)
        return -1