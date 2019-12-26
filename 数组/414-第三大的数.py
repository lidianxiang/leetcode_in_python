"""
给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

示例 1:

输入: [3, 2, 1]

输出: 1

解释: 第三大的数是 1.
示例 2:

输入: [1, 2]

输出: 2

解释: 第三大的数不存在, 所以返回最大的数 2 .
示例 3:

输入: [2, 2, 3, 1]

输出: 1

解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
存在两个值为2的数，它们都排第二。
"""


class Solution:
    """利用python的set()和remove()函数"""
    def thirdMax(self, nums):
        set_nums = set(nums)
        if len(set_nums) < 3:
            return max(set_nums)
        else:
            set_nums.remove(max(set_nums))
            set_nums.remove(max(set_nums))
            return max(set_nums)


class Solution2:
    """
    维护一个长度为三的降序数组，遍历整个nums，
    如果有比数组中最小的数字大的则将数组最后一位pop，
    然后添加新的数字。最后输出最小的即可。
    """
    def thirdMax(self, nums):
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        elif len(nums) == 3:
            return min(nums)

        res = nums[:3]
        res = sorted(res, reverse=1)
        for x in nums[3:]:
            if x > res[-1]:
                res.pop()
                res.append(x)
                res = sorted(res, reverse=1)
        return res[-1]
