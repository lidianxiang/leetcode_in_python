"""
给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。

你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

示例 1:

输入: [1, 2, 2, 3, 1]
输出: 2
解释:
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.
示例 2:

输入: [1,2,2,3,1,4,2]
输出: 6
"""


class Solution:
    def findShortestSubArray(self, nums):
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left:
                # left存储第一次出现的数的索引
                left[x] = i
            # right存储最后一次该数出现的索引
            right[x] = i
            # 统计该数的次数
            count[x] = count.get(x, 0) + 1
        # 初始化最后答案，为len(nums)
        ans = len(nums)
        # 取出出现频率最高的数
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                # 最后的答案就是第一次出现的位置与最后一次出现的位置的差值加一
                ans = min(ans, right[x] - left[x] + 1)
        return ans
