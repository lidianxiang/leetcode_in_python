"""
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
"""


class Solution:
    """动态规划，值得注意的是：要考虑到数组中的两个负数的乘积的情况，所以要考虑最小值和最大值两种情况"""
    def maxProduct(self, nums):
        if not nums:
            return

        res = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(cur_max, res)
            pre_max = cur_max
            pre_min = cur_min
        return res


class Solution2:
    """
    1、当负数个数为偶数时候, 全部相乘一定最大
    2、当负数个数为奇数时候, 它的左右两边的负数个数一定为偶数, 只需求两边最大值
    3、当有0情况,重置就可以了
    """
    def maxProduct(self, nums):
        reverse_nums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            reverse_nums[i] *= reverse_nums[i - 1] or 1
        return max(nums + reverse_nums)
