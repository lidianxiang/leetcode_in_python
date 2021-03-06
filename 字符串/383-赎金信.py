"""
给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true ；否则返回 false。

(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)

注意：

你可以假设两个字符串均只含有小写字母。

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""


class Solution:
    """巧用collections.Counter()函数"""
    def canConstruct(self, ransomNote, magazine):
        from collections import Counter

        a = Counter(ransomNote)
        b = Counter(magazine)
        return a & b == a


class Solution2:
    """使用正则表达式"""
    def canConstruct(self, ransomNote, magazine):

        import re

        # 遍历ransonNote字符串
        for i in ransomNote:
            if i in magazine:
                # 使用re.sub()函数替换ransomNote中出现的字符
                magazine = re.sub(i, '', magazine, 1)
            else:
                return False
        return True

