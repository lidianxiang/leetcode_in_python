"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
"""


class Solution:
    def rotate(self, nums, k):
        """
        拼接法
        """
        # 此处的k要进行取余操作，要考虑到k可能大于len(nums)的情况
        k %= len(nums)

        nums[:] = nums[-k:] + nums[:-k]


class Solution2:
    def rotate(self, nums, k):
        """三重旋转"""
        k %= len(nums)

        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]


class Solution3:
    """
    1、首先选定一个目标元素，找到这个元素的移位后位置，替换掉当前位置的元素
    2、被替换掉的元素成为下一个目标元素
    3、不断循环，记录次数，达到数组长度是，全部元素已经在正确位置上
    4、[1,2,3,4] k = 2时， 目标元素：1->3->1->3， 总是在已完成目标循环
    5、设置两个while循环，若不出现循环，则在内层while走完，若出现循环，则回到循环起点时跳出，下一元素成为目标元素

    """
    def rotate(self, nums, k):
        size = len(nums)
        k %= size
        # start是当出现循环时最开始的点
        count = start = 0
        while count < size:
            target = start
            tmp = nums[start]
            while True:
                target = (target + k) % size
                tmp, nums[target] = nums[target], tmp
                count += 1
                if count >= size or target == start:
                    break  # 次数到了或是出现循环则跳出
            start += 1
