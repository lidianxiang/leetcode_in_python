"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
"""


class Solution:
    def reverse(self, x):
        # python的//操作是向下取整，导致正负数取余操作结果不一致，需要将负数转为正数
        y, res = abs(x), 0
        # python int类型的范围是:[-2**31, 2*31-1]
        boundry = (1 << 31) - 1 if x > 0 else 1 << 31
        while y != 0:
            # 反转数字
            res = res * 10 + y % 10
            # 超过边界，返回0
            if res > boundry:
                return 0
            y //= 10
        return res if x > 0 else -res
