"""
有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。

现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束。

示例 1:

输入:
bits = [1, 0, 0]
输出: True
解释:
唯一的编码方式是一个两比特字符和一个一比特字符。所以最后一个字符是一比特字符。
示例 2:

输入:
bits = [1, 1, 1, 0]
输出: False
解释:
唯一的编码方式是两比特字符和两比特字符。所以最后一个字符不是一比特字符。
"""


class Solution:
    def isOneBitCharacter(self, bits):
        index = 0
        n = len(bits)
        while index < n:
            # 当index到达最后一位且最后一位是0，则为True(1比特字符)
            if bits[index] == 0 and index == n - 1:
                return True
            # 当index的字符为0，则向后移动一位
            if bits[index] == 0:
                index += 1
            # 当index的字符为1，则向后移动两位
            if bits[index] == 1:
                index += 2
        # 否则为false，即2比特字符
        return False


class Solution2:
    """
    我们可以对bits数组从左到右扫描来判断最后一位是否为一比特字符。
    当扫描到第i位时，如果bits[i]=1，那么说明这是一个两比特字符，将i的值增加 2。
    如果bits[i]=0，那么说明这是一个一比特字符，将i的值增加 1。
    """
    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        # 如果i最终落在了bits.length−1 的位置，那么说明最后一位一定是一比特字符。
        return i == len(bits) - 1


class Solution3:
    """
    三种字符分别为 0，10 和 11，那么bits数组中出现的所有 0 都表示一个字符的结束位置（无论其为一比特还是两比特）。
    因此最后一位是否为一比特字符，只和他左侧出现的连续的 1 的个数（即它与倒数第二个 0 出现的位置之间的 1 的个数，
    1、如果bits数组中只有 1 个 0，那么就是整个数组的长度减一有关。
    2、如果 1 的个数为偶数个，那么最后一位是一比特字符，
    3、如果 1 的个数为奇数个，那么最后一位不是一比特字符。
    """
    def isOneBitCharacter(self, bits):
        parity = bits.pop()
        while bits and bits.pop():
            parity ^= 1
        return parity == 0

