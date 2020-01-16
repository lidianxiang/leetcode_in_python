"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.
"""
import collections


class Solution:
    def firstUniqChar(self, s):
        count = collections.Counter(s)

        for idx, value in enumerate(s):
            if count[value] == 1:
                return idx
        return -1


from collections import OrderedDict


class Solution2:
    def firstUniqChar(self, s):
        # 新建一个有序字典
        odict = OrderedDict()
        # 计算字符串中每个元素出现的次数
        for c in s:
            odict[c] = odict[c] + 1 if c in odict else 1
        # 遍历字典
        for k, v in odict.items():
            # 寻找第一个只出现一次的字符
            if v == 1:
                # 返回其索引
                return s.index(k)
        return -1


class Solution3:
    """
    1、已知字符串由小写字母构成，则遍历a-z
    2、分别从目标的字符串头和字符串尾查找对应字母的索引；如果两索引相等，则说明是单一字符
    3、从该索引和此前遍历记录的最小索引中选出新的最小索引
    4、遍历结束后，最小索引即为进行26次遍历返回的最小索引值
    """
    def firstUniqueChar(self, s):
        min_unique_char_index = len(s)

        for c in 'abcdefghijklmnopqrstuvwxyz':
            i = s.find(c)
            if i != -1 and i == s.rfind(c):
                min_unique_char_index = min(min_unique_char_index, i)
        return min_unique_char_index if min_unique_char_index != len(s) else -1
