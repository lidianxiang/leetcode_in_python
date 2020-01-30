"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
"""


class Solution:
    """
    荷兰国旗问题：
        我们用三个指针（p0, p2 和curr）来分别追踪0的最右边界，2的最左边界和当前考虑的元素。
        沿着数组移动 curr 指针，若nums[curr] = 0，则将其与 nums[p0]互换；若 nums[curr] = 2 ，则与 nums[p2]互换。
    """
    def sortColors(self, nums):
        p0 = curr = 0
        p2 = len(nums) - 1
        while curr <= p2:
            if nums[curr] == 0:
                # 交换第curr个和第p0个元素，将指针都向右移
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                # 交换第curr个和第p2个元素，并将p2指针左移
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                # 指针curr右移
                curr += 1

