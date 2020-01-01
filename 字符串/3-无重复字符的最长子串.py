"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""


class Solution:
    """滑动窗口"""
    def lengthOfLongestSubstring(self, s):
        # 边界条件判定
        if not s:
            return 0

        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        # 遍历字符串
        for i in range(n):
            # 当前最长子串加一
            cur_len += 1
            # 当前遍历的字符在lookup集合中
            while s[i] in lookup:
                # 在lookup集合中删去最左边的字符，也是最开始的字符
                lookup.remove(s[left])
                # 窗口右移一位
                left += 1
                # 当前最长子串长度减一
                cur_len -= 1
            # 如果当前最长子串大于最大子串长度，更新最大子串长度
            if cur_len > max_len:
                max_len = cur_len
            # lookup集合添加当前字符
            lookup.add(s[i])
        return max_len
