"""
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:

输入: s = "egg", t = "add"
输出: true
示例 2:

输入: s = "foo", t = "bar"
输出: false
示例 3:

输入: s = "paper", t = "title"
输出: true
"""


class Solution:
    """
    1、str类型数据拥有内置函数index(),输入一个子字符串，可以返回子字符串在str中第一次出现的索引
    2、map将会对(参数2：可迭代对象)中的每个元素运用并将结果按照顺序存在一个迭代器里面
    3、'*'可以对对象解包，[*map...] == list(map())
    """
    def isIsomorphic(self, s, t):
        return [*map(s.index, s)] == [*map(t.index, t)]


class Solution2:
    """哈希表"""
    def isIsomorphic(self, s, t):
        # 哈希表，key为s，value为t
        hash_map = {}
        for a, b in zip(s, t):
            if a not in hash_map and b in hash_map.values():
                return False
            if a in hash_map and b != hash_map[a]:
                return False
            hash_map[a] = b
        return True
