"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
"""


class Solution:
    """
    Sunday算法：
        1、若匹配：则返回当前idx
        2、不匹配：则查看待匹配字符串的后一位字符c：
            a 若c存在于pattern中，则idx = idx + 偏移表[c]
            b 否则，idx = idx + len(pattern)
    """
    def strStr(self, haystack, needle):
        # 计算偏移表
        def calShiftMat(st):
            dic = {}
            for i in range(len(st)-1, -1, -1):
                if not dic.get(st[i]):
                    dic[st[i]] = len(st) - i
                dic['ot'] = len(st) + 1
            return dic
        # 特判
        if len(needle) > len(haystack):
            return -1
        # 特判
        if needle == "":
            return 0
        # 初始化偏移表
        dic = calShiftMat(needle)
        idx = 0

        while idx+len(needle) <= len(haystack):
            # 待匹配的子字符串
            str_cut = haystack[idx:idx+len(needle)]
            # 若待匹配的子字符串与needle正好相匹配，则返回最开始的索引值idx
            if str_cut == needle:
                return idx
            else:
                # 若匹配到最后了还没匹配上，则返回-1
                if idx+len(needle) >= len(haystack):
                    return -1
                # 不匹配的情况下，根据下一个字符的偏移，移动idx
                cur_c = haystack[idx+len(needle)]
                if dic.get(cur_c):
                    idx += dic[cur_c]
                else:
                    idx += dic['ot']
        return -1 if idx+len(needle) >= len(haystack) else idx


class Solution2:
    """巧用str.index()函数"""
    def strStr(self, haystack, needle):
        return haystack.index(needle) if needle in haystack else -1


class Solutio3:
    """暴力求解"""
    def strStr(self, haystack, needle):
        # 特判
        if not needle:
            return 0
        n1 = len(haystack)
        n2 = len(needle)
        if n1 < n2:
            return -1

        # 定义匹配函数
        def helper(idx):
            haystack_p = idx
            needle_q = 0
            while needle_q < n2:
                if haystack[haystack_p] != needle[needle_q]:
                    return False
                else:
                    haystack_p += 1
                    needle_q += 1
            return True

        # 逐一匹配
        for i in range(n1 - n2 + 1):
            if helper(i):
                return i
        return -1
