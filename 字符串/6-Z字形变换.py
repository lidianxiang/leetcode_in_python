"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
"""


class Solution:
    """
    1、字符串 s 是以 ZZ 字形为顺序存储的字符串，目标是按行打印。
    2、设 numRows 行字符串分别为 s_1, s_2,..., s_n，则容易发现：按顺序遍历字符串 s 时，
       每个字符 c 在 ZZ 字形中对应的 行索引 先从 s_1增大至 s_n，再从 s_n减小至 s_1…… 如此反复。
    3、因此，解决方案为：模拟这个行索引的变化，在遍历 s 中把每个字符填到正确的行 res[i] 。
    """
    def convert(self, s, numRows):
        if numRows < 2:
            return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            # 第一行和最后一行时，需要改变顺序
            if i == 0 or i == numRows - 1:
                flag = - flag
            # 自由改变行号，0,1,...n-1,然后时n-1,n-2,...2,1,0的顺序
            i += flag
        return "".join(res)
