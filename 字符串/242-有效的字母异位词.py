"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
"""


class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        se = set(s)
        # 当s与t的set集合相同时
        if se == set(t):
            # 遍历字符串
            for i in se:
                # 计算每个字符出现的次数
                if s.count(i) != t.count(i):
                    return False
            return True
        else:
            return False


class Solution2:
    """哈希表"""
    def isAnagram(self, s, t):
        # 创建一个哈希表，key为s字符串中的字符，value为每个字符出现的次数
        dic = {}
        # 遍历s字符串
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        # 遍历t字符串
        for i in t:
            # 当t中的字符串不在dic的key中，或是key对应的value值不相等
            if i not in dic or dic[i] <= 0:
                return False
            # t中出现一个字符就在value中减一
            dic[i] -= 1
        # 遍历dic
        for i in dic:
            # 判断dic中的每个key对应的value是否为0，如果不是，则返回False，否则返回True
            if dic[i] != 0:
                return False
        return True
