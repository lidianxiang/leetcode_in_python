"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定 nums = [1,1,1,2,2,3],

函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,1,2,3,3],

函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。

你不需要考虑数组中超出新长度后面的元素。
"""


class Solution:
    """删除多余的重复项"""
    def removeDuplicates(self, nums):
        # 数字的下标索引i， count计数
        i, count = 1, 1
        while i < len(nums):
            # 因为数组是先排序的，若相邻的两个元素相等
            if nums[i] == nums[i-1]:
                # 计数count加一
                count += 1
                # 若count超过2
                if count > 2:
                    # 直接原地删除多余的重复元素
                    nums.pop(i)
                    # 索引值减去一
                    i -= 1
            # 相邻的数组不相等的情况
            else:
                count = 1
            # 索引值加一，指针向后移动
            i += 1
        return len(nums)


class Solution2:
    """覆盖多余的重复项"""
    def removeDuplicates(self, nums):
        # j指针表示去除重复项的的长度
        # count为计数
        j, count = 1, 1
        # 遍历数组
        for i in range(1, len(nums)):
            # 数组中相邻元素相等的情况
            if nums[i] == nums[i - 1]:
                count += 1
            # 数组中相邻元素不相等的情况
            else:
                count = 1
            # 当count计数小于等于2时
            if count <= 2:
                # i指针所指向的元素移动到j位置，并同时增加i和j
                nums[j] = nums[i]
                j += 1
        return j
