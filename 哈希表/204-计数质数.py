"""
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""


class Solution:
    """
    埃拉托斯特尼筛法
    """
    def countPrimes(self, n):
        # 当n小于2时，是没有质数的，直接返回0
        if n < 2:
            return 0

        isPrime = [1] * n
        # 数字0和数字1不是质数，所以计数为0
        isPrime[0] = isPrime[1] = 0
        # 遍历数字2，根号i+1的范围
        for i in range(2, int(n**0.5)+1):
            # 表示判断第i个数是否已经被赋值为0，排除掉不是质数的数，不再进行二次排除
            if isPrime[i]:
                # 指定步长，进行列表切片赋值，之所以从i的平方开始，是因为小于i的平方的倍数已经排除掉了
                isPrime[i*i:n:i] = [0] * ((n-1 - i*i) // i + 1)
        return sum(isPrime)
