"""
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:

输入: "hello"
输出: "holle"
示例 2:

输入: "leetcode"
输出: "leotcede"
"""


class Solution:
    """双指针"""
    def reverseVowels(self, s: str):
        s = list(s)
        # print(s)
        vowels = 'aAeEiIoOuU'
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            # 当左右指针所指的字符都是元音时，调换两者的顺序
            elif s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(s)

