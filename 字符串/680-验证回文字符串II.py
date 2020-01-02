"""
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:

输入: "aba"
输出: True
示例 2:

输入: "abca"
输出: True
解释: 你可以删除c字符。

"""


class Solution:
    def validPalindrome(self, s):
        p1, p2 = 0, len(s)-1
        while p1 < p2:
            if s[p1] != s[p2]:
                # 舍弃左字符
                a = s[p1+1:p2+1]
                # 舍弃右字符
                b = s[p1:p2]
                return a[::-1] == a or b[::-1] == b
            p1 += 1
            p2 -= 1
        return True
