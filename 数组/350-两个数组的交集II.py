"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
"""


class Solution:
    """
    排序 + 双指针法
    """
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        res = []
        left, right = 0, 0
        while left < len(nums1) and right < len(nums2):
            if nums1[left] < nums2[right]:
                left += 1
            elif nums1[left] == nums2[right]:
                res.append(nums1[left])
                left += 1
                right += 1
            else:
                right += 1
        return res


import collections


class Solution2:
    """哈希表"""
    def intersect(self, nums1, nums2):
        # 将长度短的数组存入哈希表中，减少内存
        # 假定nums1的长度小于nums2的长度
        # 如果nums2的长度大于nums1的长度时，应该调换两者顺序
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        # 新建一个字典
        lookup = collections.defaultdict(int)
        # 将nums1中的元素存入字典中
        for i in nums1:
            lookup[i] += 1

        res = []
        # 遍历nums2数组
        for i in nums2:
            if lookup[i] > 0:
                res.append(i)
                lookup[i] -= 1
        return res
