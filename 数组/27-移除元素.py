"""
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:

给定 nums = [3,2,2,3], val = 3,

函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,1,2,2,3,0,4,2], val = 2,

函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

注意这五个元素可为任意顺序。

你不需要考虑数组中超出新长度后面的元素。

"""


class Solution:
    def removeElement(self, nums, val):
        # 定义一个指针，从零开始
        cur = 0
        # 遍历数组
        while cur < len(nums):
            # 当指针所指的数值等于val的值
            if nums[cur] == val:
                # 原地移除这个数
                nums.pop(cur)
            else:
                # 否则（指针所指的数与val的值不相等），cur指针向后移动一位
                cur += 1
        # 返回最后的数组长度
        return len(nums)


class Solution2:
    """双指针法
    设置双指针 i 和 j，其中，j 用于寻找非 val 元素，来覆盖 i 所指向的元素。

    初始时：设 i = 0, j = 0
    遍历数组：
        若 nums[j] != val：
            把 j 的值赋给 i：nums[i] = nums[j]
            同步增长双指针：i = i + 1, j = j + 1
        若 nums[j] == val：
            j 变为快指针：j = j + 1，寻找下一个非 val 元素

    """
    def removeElement(self, nums, val):
        length = len(nums)
        i, j = 0, 0
        while j < length:
            if nums[j] != val:
                # 把 j 的值赋给 i
                nums[i] = nums[j]
                i += 1
                j += 1
            else:
                # j 变为快指针
                j += 1

        return length - (j - i)
