"""
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
"""


class Solution:
    def longestValidParentheses(self, s):
        res = []
        stack = []
        # 遍历数组
        for i in range(len(s)):
            # 当出现右括号时，且栈里面有左括号
            if stack and s[i] == ')':
                # 将栈里的括号弹出
                res.append(stack.pop())
                # res再加入右括号
                res.append(i)
            # 当出现左括号，压入栈里面
            if s[i] == '(':
                stack.append(i)

        # print(res)
        # 排序
        res.sort()
        max_len = 0
        i = 0
        # 遍历排序后的res
        while i < len(res)-1:
            # 保存最长连续连续子序列的左边界
            tmp = i
            # 当左边界存在且与下一位的索引值差为1时，更新i
            while i < len(res) - 1 and res[i+1] - res[i] == 1:
                i += 1
            # 根据条件更新max_len
            max_len = max(max_len, i - tmp + 1)
            i += 1
        return max_len


class Solutin2:
    def longestValidParentheses(self, s):
        # 特殊条件
        if not s:
            return 0
        # 初始化栈
        stack = [-1]
        res = 0
        for i in range(len(s)):
            # 当为左括号时，压入栈
            if s[i] == '(':
                stack.append(i)
            # 当为右括号时
            else:
                # 从栈里弹出左括号
                stack.pop()
                # 当栈里面为空
                if not stack:
                    # 将右括号也也压入栈里面
                    stack.append(i)
                # 当栈里面不为空
                else:
                    # 判断更新res结果，其中i - stack[-1]便是当前位置索引减去上一个不匹配位置索引的差值
                    res = max(res, i - stack[-1])
        return res


class Solution3:
    """动态规划"""
    def longestValidParantheses(self, s):
        # 当s为空时，直接返回0
        if not s:
            return 0

        res = 0
        n = len(s)
        # dp的初始状态
        dp = [0] * n
        # 遍历字符串
        for i in range(1, n):
            # 当当前的字符为右括号时
            if s[i] == ')':
                # 当前的前一个字符为左括号时（有效括号）
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                # 当前的前一个字符为右括号时，找到上一匹配字符串的上一位 i-dp[i-1]-1
                if s[i - 1] == ')' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    # 当前位置的最长有效括号长度等于上一位有效括号的长度加上自身匹配的上一位的有效括号的长度加上二
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                # 更新res
                res = max(res, dp[i])
        return res
