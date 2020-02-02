"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
"""


class Solution:
    """贪心算法：每次找到能跳最远的位置，出现越过最后或能到最后的情况时返回跳跃次数"""
    def jump(self, nums):
        # 对于nums数组全是1的特殊情况
        if nums.count(1) == len(nums):
            return len(nums) - 1

        def fun(n):
            if not n:
                return 0
            for k, v in enumerate(n):
                if v >= len(n) - k:
                    return fun(n[:k]) + 1

        return fun(nums[:-1])


class Solution2:
    """dp"""
    def jump(self, nums):
        n = len(nums)
        if n == 0 or n == 1:
            return 0

        MAXSIZE = 9999999
        dp = [MAXSIZE] * n
        dp[0] = 0
        min_i = 0
        addstart = 0
        while dp[n - 1] == MAXSIZE:
            for j in range(min_i + addstart, min_i + nums[min_i] + 1):
                if j < n and dp[j] > dp[min_i]+ 1:
                    dp[j] = dp[min_i] + 1
            if dp[-1] != MAXSIZE:
                break

            addstart = nums[min_i]
            min_i += 1
        return dp[-1]


class Solution3:
    """贪心算法"""
    def jump(self, nums):
        # 步数
        step = 0
        # 上一步到达的边界
        end = 0
        # 能到达的最远位置
        max_bound = 0
        # range的范围为[0, n - 1),因为i==0时，step已经加一了
        for i in range(len(nums) - 1):
            # 更新能到达的最远位置
            # 上一最远位置和当前索引i上的步数之和中的较大者
            max_bound = max(max_bound, nums[i] + i)
            if i == end:
                step += 1
                end = max_bound
        return step
