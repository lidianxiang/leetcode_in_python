"""
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：

给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
说明:

你可以假设数组不可变。
会多次调用 sumRange 方法。
"""


class NumArray:
    """
    动态规划
        1、若数组为空，直接返回
        2、初始化dp=[0,0,...,0],长度为n+1
        3、遍历数组，保存累加和，遍历区间为[2, n+1)：
            dp[i] = nums[i-1] + dp[i-1]
        4、索引i到j间的区域和公式为：dp[j+1] - dp[i]
    注意： dp[i]表示到i-1索引处的累加和。
    """

    def __init__(self, nums):
        if not nums:
            return
        n = len(nums)
        self.dp = [0] * (n + 1)
        self.dp[1] = nums[0]
        for i in range(2, n + 1):
            self.dp[i] = nums[i - 1] + self.dp[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j + 1] - self.dp[i]

