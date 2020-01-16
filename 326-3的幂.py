"""
给定一个整数，写一个函数来判断它是否是 3 的幂次方。

示例 1:

输入: 27
输出: true
示例 2:

输入: 0
输出: false
示例 3:

输入: 9
输出: true
示例 4:

输入: 45
输出: false
"""

import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 3 ** round(math.log(n,3)) == n


class Solution2:
    """
    递归
    """
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        # 3的0次方
        elif n == 1:
            return True
        else:
            # 当n不是3的倍数时，直接返回False
            if n % 3 != 0:
                return False
            else:
                # 当n是3的倍数且n除以3等于1（即3）
                s = n / 3
                if s == 1:
                    return True
                else:
                    # 递归调用函数
                    return self.isPowerOfThree(s)
