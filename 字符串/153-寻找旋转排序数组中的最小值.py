"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。

示例 1:

输入: [3,4,5,1,2]
输出: 1


示例 2:

输入: [4,5,6,7,0,1,2]
输出: 0
"""


class Solution:
    def findMin(self, nums):
        nums.sort()
        return nums[0]


class Solution2:
    def findMin(self, nums):
        min_value = nums[0]
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                min_value = nums[i+1]
        return min_value


class Solution3:
    """二分查找"""
    def findMin(self, nums):
        # 当nums只有一个元素时，直接返回第一个也是唯一的一个元素值
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1
        # 当数组的最后一个元素大于第一个元素，证明数组有升序排列的有序数组，直接返回第一个元素，即为最小元素
        if nums[right] > nums[0]:
            return nums[0]

        while right >= left:
            # 找到中点
            mid = left + (right - left) // 2
            # 当中点值大于中点的下个元素值，即证明中点的下个元素为翻转点，即最小值
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # 当中点的前一个元素值小于元素值，即证明中点的前一个元素值为翻转点，即最小值
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            # 当中点值大于第一个元素值，则需要从mid的右侧搜索，直接放弃mid的左侧
            if nums[mid] > nums[0]:
                left = mid + 1
            # 当中点值小于第一个元素值，则需要从mid的左侧搜索，直接放西mid的右侧
            else:
                right = mid - 1

