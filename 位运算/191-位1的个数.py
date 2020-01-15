"""
编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。

 

示例 1：

输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
示例 2：

输入：00000000000000000000000010000000
输出：1
解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
示例 3：

输入：11111111111111111111111111111101
输出：31
解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


class Solution2:
    """十进制转二进制的方式，每次对2取余判断是否为1，是的话count加一"""
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            res = n % 2
            if res == 1:
                count += 1
            n //= 2
        return count


class Solution3:
    """把n与1进行位运算，将得到n的最低位数字。因此可以取出最低位数，在将n右移一位。循环次步骤，直到n等于0"""
    def hammingWeight(self, n):
        count = 0
        while n:
            # n & 1 等价于 n % 2 == 1(判断是否位奇数)
            count += n & 1
            # n 右移一位
            n >>= 1
        return count


class Solution4:
    def hammingWeight(self, n):
        # 结果
        res = 0
        mask = 1
        # python整型为32为
        for i in range(32):
            # n & 1 等价于 n % 2 == 1
            if n & mask:
                # 计数加一
                res += 1
            # mask左移一位
            mask = mask << 1
        return res


class Solution5:
    def hammingWeight(self, n):
        count = 0
        while n != 0:
            count += 1
            # 这步操作的意思是： 消除掉n中最后的为1的位置
            n &= n - 1
        return count
