"""
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
"""


class Solution:
    """动态规划（自上而下）"""
    def isMatch(self, s, p):
        # 备忘录
        memo = dict()

        def dp(i, j):
            """

            :param i: 表示当前s的匹配位置
            :param j: 表示当前p的匹配位置
            :return:
            """
            if (i, j) in memo:
                return memo[(i, j)]
            # 表示p已经匹配完了，若s还有字符尚未匹配则返回False，否则表示s也已经匹配完成，返回True
            if j == len(p):
                return i == len(s)
            # first表示当前s，p的首位是否匹配，p[j]是否为s[i]或是星号
            # i < len(s）表示s是否遍历完
            first = i < len(s) and p[j] in {s[i], '.'}
            # 当j中存在星号且j的长度小于总长度减2
            if j <= len(p) - 2 and p[j+1] == '*':
                # 跳过这两个字符，表示匹配0次
                ans = dp(i, j+2) or first and dp(i+1, j)
            else:
                # 若j中不存在星号时，继续向后匹配
                ans = first and dp(i+1, j+1)
            # 缓存值备忘录
            memo[(i, j)] = ans
            return ans
        return dp(0, 0)
