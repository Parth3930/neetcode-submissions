class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        total = len(nums1) + len(nums2)
        half = (total + 1) // 2

        left = 0
        right = len(nums1)

        while left <= right:

            partition1 = (left + right) // 2
            partition2 = half - partition1

            left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            right1 = float('inf') if partition1 == len(nums1) else nums1[partition1]

            left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            right2 = float('inf') if partition2 == len(nums2) else nums2[partition2]

            if left1 <= right2 and left2 <= right1:

                if total % 2:
                    return max(left1, left2)

                return (max(left1, left2) + min(right1, right2)) / 2

            elif left1 > right2:
                right = partition1 - 1

            else:
                left = partition1 + 1