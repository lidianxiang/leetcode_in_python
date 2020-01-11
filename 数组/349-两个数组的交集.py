"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [9,4]
"""


class Solution:
    """利用set()集合性质"""
    def intersection(self, nums1, nums2):
        a, b = set(nums1), set(nums2)
        return list(a & b)


class Solution2:
    """哈希表，额外申请空间"""
    def intersection(self, nums1, nums2):
        dic = {}
        for i in nums1:
            if not dic.get(i):
                dic[i] = 1
        # 创建一个list列表，用于存储相同的数据
        new = list()
        for i in nums2:
            if dic.get(i):
                new.append(i)
                dic[i] -= 1
        return new


class Solution3:
    """哈希表，不使用额外的空间"""
    def intersection(self, nums1, nums2):
        # 特判
        if not nums1 or not nums2:
            return []

        dic = {}
        for i in nums1:
            if not dic.get(i):
                dic[i] = 1

        n = len(nums2)
        i, j = 0, n - 1
        while i < j:
            # 当nums2中的元素在dic中，则将dic中的value减去
            if dic.get(nums2[i]):
                dic[nums2[i]] -= 1
                # i向后移动一位
                i += 1
            # 当nums2中的元素不在dic中
            else:
                # 将不在dic的元素向与nums2最后的元素调换位置，使得与nums1中相同的元素放在nums2的前面
                nums2[i], nums2[j] = nums2[j], nums2[i]
                j -= 1
        if dic.get(nums2[i]):
            i += 1
        return nums2[:i]

