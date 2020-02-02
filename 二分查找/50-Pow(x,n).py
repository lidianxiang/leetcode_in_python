"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
"""


class Solution:
    """利用二分查找思想，每次记录连乘的次数count，每次倍乘"""
    def myPow(self, x, n):
        def re_binarySearch(x, n):
            if n < 1:
                return 1
            count, sums = 1, x
            while count * 2 <= n:
                count += count
                sums *= sums
            return re_binarySearch(x, n-count) * sums
        res = re_binarySearch(abs(x), abs(n))
        res = -res if x < 0 and n % 2 != 0 else res
        res = 1/res if n < 0 else res
        return res
