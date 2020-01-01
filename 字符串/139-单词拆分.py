"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""


class Solution:
    """
    动态规划：
        1、初始化dp=[False, False, ...,False],长度为n+1，dp[i]表示s的前i位时候可以用wordDict中的单词表示
        2、初始化dp[0]=True，空字符可以被表示
        3、遍历字符串，区间为[0,n)
            遍历字符串，区间为[i+1, n+1)
                若dp[i]=True且s[i,j)在wordDict中，则dp[j]=True
        4、返回dp[n]
    """

    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]


class Solution2:
    """记忆化回溯"""
    def wordBreak(self, s, wordDict):
        import functools
        @functools.lru_cache(None)
        def back_track(s):
            # s为零，表示已经使用wordDict中的单词分割完
            if not s:
                return True
            # 初始化结果为False
            res = False
            # 遍历
            for i in range(1, len(s) + 1):
                # 若s[0,...,i-1]在wordDict中，则使用回溯
                if s[:i] in wordDict:
                    res = back_track(s[i:]) or res
            return res

        return back_track(s)
