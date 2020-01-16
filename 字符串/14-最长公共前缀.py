"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
"""


class Solution:
    """
    巧用python的zip()函数
    """
    def longestCommonPrefix(self, strs):
        s = ""
        for i in zip(*strs):
            # 当每个字符串的第i个字符联立后的长度等于一，即为同一个元素
            if len(set(i)) == 1:
                s += i[0]
            else:
                break
        return s


class Solution2:
    def longestCommonPrefix(self, strs):
        # 特判
        if not strs:
            return ""
        # 假定最后的结果为第一个字符串
        res = strs[0]
        # 计数
        i = 1
        # 遍历数组（所有的字符串）
        while i < len(strs):
            # 和后面单词比较，看res与每个单词相同的最长前缀是多少
            while strs[i].find(res) != 0:
                res = res[:len(res) - 1]
            i += 1
        return res


class Solution3:
    """按字典排序数组，比较第一个，和最后一个单词，有多少前缀相同"""
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        strs.sort()
        a, b = strs[0], strs[len(strs) - 1]
        res = ""
        for i in range(len(a)):
            if i < len(b) and a[i] == b[i]:
                res += a[i]
            else:
                break
        return res
