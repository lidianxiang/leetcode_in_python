"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
"""


class Solution:
    """
    1、找到旋转的下标，使用二分查找
    2、在选中区域内再次使用二分查找
    """

    def search(self, nums: List[int], target: int) -> int:
        def find_rotate_index(left, right):
            if nums[left] < nums[right]:
                return 0
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot - 1
                    else:
                        left = pivot + 1

        def search(left, right):
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] == target:
                    return pivot
                else:
                    if target < nums[pivot]:
                        right = pivot - 1
                    else:
                        left = pivot + 1
            return -1

        n = len(nums)
        # 两种特殊情况先行判断
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1

        rotate_index = find_rotate_index(0, n - 1)

        if nums[rotate_index] == target:
            return rotate_index
        if rotate_index == 0:
            return search(0, n - 1)
        if target < nums[0]:
            return search(rotate_index, n - 1)

        return search(0, rotate_index)
