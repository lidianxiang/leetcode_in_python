"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
"""


class Solution:
    """模拟相加运算过程"""
    def addStrings(self, num1, num2):
        # 结果保存
        res = ""
        # 从末尾（个位）开始计算，carruy表示是否要进位
        i, j, carry = len(num1)-1, len(num2)-1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            # 进位更新
            carry = tmp // 10
            # 结果更新
            res = str(tmp % 10) + res
            # 两个指针向前移动
            i, j = i - 1, j - 1
        # 要考虑最开始（头部）是否存在进位的情况
        return "1" + res if carry else res
