"""
给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
示例 1:

输入: "A"
输出: 1
示例 2:

输入: "AB"
输出: 28
示例 3:

输入: "ZY"
输出: 701

"""


class Solution:
    def titleToNumber(self, s: str) -> int:
        dic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
               'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23,
               'X': 24, 'Y': 25, 'Z': 26}
        if len(s) == 1:
            return dic[s]

        length = len(s)
        result = 0
        for i in range(length - 1, -1, -1):
            result += dic[s[length - i - 1]] * (26 ** i)
        return result


# 26进制转10进制
class Solution2:
    def titleToNumber(self, s: str) -> int:
        # 倒序字符串
        s = s[::-1]
        result = 0
        for i in range(len(s)):
            # ord()函数是将字符串转换为ascii码，因为此处的A为1，故而需要减去64才能对应
            result += (ord(s[i]) - 64) * (26 ** i)
        return result
