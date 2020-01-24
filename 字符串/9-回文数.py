"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
"""


class Solution:
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]


class Solution2:
    """
    反转一半：反转数字的后半部分，与前半部分进行比较"""
    def isPalindrome(self, x):
        # 负数不是回文数或者个位数为0但是不是数字0的情况
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev_num = 0
        while x > rev_num:
            rev_num = rev_num * 10 + x % 10
            x = x // 10
        return x == rev_num or x == rev_num // 10
