"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0

"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 当 target小于最小值(nums[0]),将target插入到最开始
        if target < nums[0]:
            return 0
        # 当 target大于最大数(nums[-1])，将target插入到最后面
        if target > nums[-1]:
            return len(nums)
        # 定义一个指针
        cur = 0
        # 遍历链表
        while cur < len(nums):
            # 当cur指针所指的值小于target，指针继续向后移动
            if nums[cur] < target:
                cur += 1
            # 当 cur指针所指的值大于targe35t，直接返回cur值
            else:
                return cur


class Solution2:
    """二分查找"""
    def searchInsert(self, nums: List[int], target: int) -> int:
        size = len(nums)
        # 判断特例
        if size == 0:
            return 0

        left = 0
        right = size

        while left < right:
            # 中间值mid
            mid = left + (right - left) // 2
            # 当target值大于中间值
            if nums[mid] < target:
                # 可以将范围缩小至后半部分
                left = mid + 1
            else:
                # assert 进行判断，是否符合条件target小于等于中间值
                assert nums[mid] >= target
                # 如果是的话，将范围缩小至前半部分
                right = mid
        # 返回索引值
        return left
