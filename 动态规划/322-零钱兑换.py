"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
"""


class Solution:
    """动态规划(自下而上)"""
    def coinChange(self, coins, amount):
        # 初始化这个状态初始值
        dp = [float("inf")] * (amount+1)
        # 0元钱的兑换方式为0种
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                # 要考虑到兑换的钱要大于兑换的零钱的条件
                if i >= coin:
                    # 状态转移方程，表示i元的组合方式dp[i]可以不使用这个coin或是使用了这个coin（那么dp值要加一）
                    dp[i] = min(dp[i], dp[i-coin]+1)
        # 返回最后的值，要考虑到不能完成零钱兑换的情况（返回-1）
        return dp[-1] if dp[-1] != float('inf') else -1


class Solution2:
    """记忆化回溯（自上而下）"""
    def coinChange(self, coins, amount):
        # 定义一个字典，key为amount值，vlaue表示零钱的个数
        memo = {0: 0}

        def helper(n):
            if n in memo:
                return memo[n]

            res = float('inf')
            for coin in coins:
                if n >= coin:
                    res = min(res, helper(n - coin) + 1)
            memo[n] = res
            return res

        return helper(amount) if helper(amount) != float('inf') else -1
