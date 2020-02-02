"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""


class Solution:
    """排序数组分类：维护一个映射ans:{string -> list}，其中每个键K是一个排序字符串
                   每个值是初始输入的 字符串列表，排序后等于K"""
    def groupAnagrams(self, strs):
        import collections
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        # ans = defaultdict(<class 'list'>, {
        # ('a', 'e', 't'): ['eat', 'tea', 'ate'],
        #  ('a', 'n', 't'): ['tan', 'nat'],
        # ('a', 'b', 't'): ['bat']})
        return ans.values()


class Solution2:
    """
    按计数分类：当且仅当他们的字符计数（每个字符出现的次数）相同时，两个字符串是字母异位词
    """
    def groupAnagrams(self, strs):
        import collections
        ans = collections.defaultdict(list)
        for s in strs:
            # 将每个字符串s转换为字符数count，由26个非负整数组成
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        # ans = defaultdict(<class 'list'>, {
        # (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['eat', 'tea', 'ate'],
        # (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['tan', 'nat'],
        # (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['bat']})
        return ans.values()
