"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

"""


class Solution:
    def isValid(self, s: str) -> bool:
        # 定义一个栈
        stack = []
        # hash map
        mapping = {"(":")", "[":"]", "{":"}"}
        # 遍历字符串
        for char in s:
            if char in mapping:
                # 当字符存在在mapping的键中，则加入至栈中
                stack.append(char)
            # len(stack)==0表示字符串只有‘]’,'}',')'，没有‘(','[','}'的情况，例如s=']'的情况
            # 否则弹出右括号（小、中、花）并映射到mapping中变成左括号，看看是否相等
            # elif len(stack) == 0 or mapping[stack.pop()] != char:
            elif not stack or mapping[stack.pop()] != char:
                return False
        # 最后，不是返回True，而是要判断长度是否为零
        # 要排除只有左括号的情况
        # return len(stack) == 0
        return not stack
