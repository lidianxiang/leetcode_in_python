"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

注意数组中可能存在重复的元素。

示例 1：

输入: [1,3,5]
输出: 1
示例 2：

输入: [2,2,2,0,1]
输出: 0
"""


class Solution:
    """排序"""
    def findMin(self, nums):
        nums.sort()
        return nums[0]


class Solution2:
    """遍历数组"""
    def findMin(self, nums):
        min_value = nums[0]
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                min_value = nums[i+1]
        return min_value


class Solution3:
    """二分查找"""
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            # 中点
            mid = left + (right - left) // 2
            # 当中点值大于最右侧值，说明mid在第二部分
            if nums[mid] > nums[right]:
                left = mid + 1
            # 当中点值小于最右侧值，说明mid在第一部分
            elif nums[mid] < nums[right]:
                right = mid
            # 当中点值等于最右侧值（nums数组中存在重复元素），例如[1 0 1 1 1],令right减一，使得数组不会越界
            else:
                right -= 1   # 关键点
        return nums[left]
