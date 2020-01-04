"""
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

示例 1:
s = "abc", t = "ahbgdc"

返回 true.

示例 2:
s = "axc", t = "ahbgdc"

返回 false.
"""


class Solution:
    """利用python的切片性质，从头遍历s的每个字符，若t中均存在，则s为t的子序列，否则就不是"""
    def isSubsequence(self, s, t):
        for i in s:
            if i in t:
                t = t[t.index(i)+1:]
            else:
                return False
        return True


class Solutin2:
    """
    双指针：
        1、指针point_s指向s，point_t指向t，两个指针都从索引0开始
        2、当两个指针所指向的值相同，则point_s向后移动一位
        3、否则point_t向后移动一位，继续比较两个指针所指向的值是否相同
        4、最后的判定条件是指针point_s是否指向了最后一位，即s完全比较完了

    """
    def isSubsequence(self, s, t):
        point_s = 0
        point_t = 0
        length_s = len(s)
        length_t = len(t)

        while point_s < length_s and point_t < length_t:
            if s[point_s] == t[point_t]:
                point_s += 1
            point_t += 1
        return point_s == length_s


class Solution3:
    """迭代器性质"""
    def isSubsequence(self, s, t):
        b = iter(t)
        return all(((i in b) for i in s))
