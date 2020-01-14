"""
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
"""


class largestNumKey(str):
    def __lt__(x, y):
        return x+y > y+x


class Solution:
    """将数组转换成字符串进行比较"""
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=largestNumKey))
        # 排除数组只含有0的情况
        return '0' if largest_num[0] == '0' else largest_num


