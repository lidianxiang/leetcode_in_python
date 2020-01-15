"""
不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。

示例 1:

输入: a = 1, b = 2
输出: 3
示例 2:

输入: a = -2, b = 3
输出: 1
"""


class Solution:
    """位运算模拟加减运算
    1、a + b 的问题拆分为 (a 和 b 的无进位结果) + (a 和 b 的进位结果)
    2、无进位加法使用异或运算计算得出
    3、进位结果使用与运算和移位运算计算得出
    4、循环此过程，直到进位为 0

    Tip：在 Python 中，整数不是 32 位的，也就是说你一直循环左移并不会存在溢出的现象，
        这就需要我们手动对 Python 中的整数进行处理，手动模拟 32 位 INT 整型。
    """
    def getSum(self, a: int, b: int) -> int:
        # 2 ^ 32
        MASK = 0x100000000
        # 整型的最大值
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1
        while b != 0:
            # 进位标志
            carry = (a & b) << 1
            # 异或操作并对MASK取模
            a = (a ^ b) % MASK
            # 进位结果对MASK取模
            b = carry % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)
