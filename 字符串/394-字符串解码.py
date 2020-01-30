"""
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例:

s = "3[a]2[bc]", 返回 "aaabcbc".
s = "3[a2[c]]", 返回 "accaccacc".
s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".
"""


class Solution:
    """本题的难点在于括号内嵌套括号，需要从内向外生成与拼接字符串，这与栈的先入后出特性相对应"""
    def decodeString(self, s):
        # 构建一个辅助栈stack
        stack, res, multi = [], "", 0
        # 遍历字符串
        for c in s:
            # 当字符为左括号时
            if c == '[':
                # 将当前multi与res入栈
                stack.append([multi, res])
                # 重置空与0
                res, multi = "", 0
            elif c == ']':
                # 当出现右括号，stack出栈
                cur_multi, last_res = stack.pop()
                # 拼接字符串
                res = last_res + cur_multi * res
            # 当出现数字时，将数字字符串转换为数字
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            # 当字符为字母时，直接拼接
            else:
                res += c
        return res


class Solution2:
    """递归法"""
    def decodeString(self, s):
        def dfs(string, i):
            res, multi = "", 0
            while i < len(string):
                # 当字符为数字时，转换为int类型
                if '0' <= string[i] <= '9':
                    multi = multi * 10 + int(string[i])
                # 当字符为左括号时
                elif string[i] == '[':
                    # 开启新一轮递归
                    i, tmp = dfs(string, i + 1)
                    # 结果拼接
                    res += multi * tmp
                    # 记录数字的multi置零
                    multi = 0
                # 当字符为右括号时
                elif string[i] == ']':
                    # 返回当前的字符与索引
                    return i, res
                else:
                    res += string[i]
                # 索引前进一位
                i += 1
            return res

        return dfs(s, 0)
