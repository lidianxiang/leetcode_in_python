"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        # 假定nums1数组的长度较小，如果nums1的长度比nums2的长度长的话，需调换两者的顺序
        if m > n:
            # nums1, nums2, m, n = nums2, nums1, n, m
            return self.findMedianSortedArrays(nums2, nums1)
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m+n+1)//2
        # 遍历数组nums1（nums1的长度较短），相对nums2来说的话，时间搜索更快
        # 我们遍历数组nums1，是要找到一个临界条件，使得nums1[i] >= nums2[j-1], nums1[i-1] <= nums2[j]
        while imin <= imax:
            # i 从nums1的中位数开始
            i = (imin + imax) // 2
            j = half_len - i
            # 根据nums1[i]、nums1[i-1]、nums2[j-1]和nums2[j]的关系调整i的边界
            if i < m and nums2[j-1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            # 找到合适的i边界时
            else:
                if i == 0: # 确定左边界情况
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])

                if (m+n) % 2 == 1: # 奇数的情况
                    return max_of_left

                if i == m: # 确定右边界的情况
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                return (max_of_left + min_of_right) / 2
