"""
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true
示例 2:

输入:pattern = "abba", str = "dog cat cat fish"
输出: false
示例 3:

输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false
示例 4:

输入: pattern = "abba", str = "dog dog dog dog"
输出: false
"""


class Solution:
    """巧用map()函数"""
    def wordPattern(self, pattern, str):
        res = str.split()
        return list(map(pattern.index, pattern)) == list(map(res.index, res))


class Solution2:
    """
    第一步 key为pattern, value为words, 遍历pattern, 检查同一个patten是否对应相同的word
    第二步 key为words, value为pattern, 遍历words, 检查同一个word是否对应相同的patter
    """
    def wordPattern(self, pattern, str):
        words = str.split()
        hash_table_pattern = {}
        hash_table_words = {}

        if len(words) != len(pattern):
            return False

        for i, letter in enumerate(pattern):
            if hash_table_pattern.get(letter):
                if hash_table_pattern[letter] != words[i]:
                    return False
            else:
                hash_table_pattern[letter] = words[i]

        for i, word in enumerate(words):
            if hash_table_words.get(word):
                if hash_table_words[word] != pattern[i]:
                    return False
            else:
                hash_table_words[word] = pattern[i]
        return True
