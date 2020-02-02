"""
给一非空的单词列表，返回前 k 个出现次数最多的单词。

返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。

示例 1：

输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
输出: ["i", "love"]
解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
    注意，按字母顺序 "i" 在 "love" 之前。
 

示例 2：

输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
输出: ["the", "is", "sunny", "day"]
解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
    出现次数依次为 4, 3, 2 和 1 次。
"""


class Solution:
    def topKFrequent(self, words, k):
        from collections import Counter
        count = Counter(words)
        # print(count)
        candidates = count.keys()
        # key中的匿名函数表示：按照单词出现的频率高低排序，如果频率相同则根据字母顺序排序
        candidates = sorted(candidates, key=lambda w: (-count[w], w))
        return candidates[:k]


class Solution2:
    """堆排序"""
    def topKFrequent(self, words, k):

        import collections
        import heapq
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]




