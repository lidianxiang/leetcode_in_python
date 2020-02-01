"""
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

 

示例 1：

输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]
"""


class Solution:
    """因为单词长度固定，可以计算出截取字符串的单词个数是否和words里相等，
       可以借助哈希表，一个哈希表是words，一个哈希表是截取的字符串，然后进行比较是否相等"""
    def findSubstring(self, s, words):
        from collections import Counter
        # 特判
        if not s or not words:
            return []

        one_word = len(words[0])
        all_len = len(words) * one_word
        n = len(s)
        words = Counter(words)
        res = []
        # 遍历s字符串，从0开始
        for i in range(0, n - all_len + 1):
            tmp = s[i:i+all_len]
            c_tmp = []
            # 以words的长度为准，步长为words中单个单词的长度，遍历截取的s字符串
            for j in range(0, all_len, one_word):
                c_tmp.append(tmp[j:j+one_word])
            # 比较两者的哈希表的键值对是否相等，若相等，则添加s中的起始位置
            if Counter(c_tmp) == words:
                res.append(i)
        return res


class Solution2:
    """滑动窗口：始终维护着所有单词长度总和的一个长度队列"""
    def findSubString(self, s, words):
        from collections import Counter
        # 特判
        if not s or not words:
            return []

        one_word = len(words[0])
        word_num = len(words)
        n = len(s)
        words = Counter(words)
        res = []
        for i in range(one_word):
            cur_cnt = 0
            left = i
            right = i
            cur_Counter = Counter()
            while right + one_word <= n:
                w = s[right:right + one_word]
                right += one_word
                cur_Counter[w] += 1
                cur_cnt += 1
                while cur_Counter[w] > words[w]:
                    left_w = s[left:left + one_word]
                    left += one_word
                    cur_Counter[left_w] -= 1
                    cur_cnt -= 1
                if cur_cnt == word_num:
                    res.append(left)
        return res


