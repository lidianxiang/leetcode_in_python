"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
"""


class Solution:
    """
    贪心算法
        1、定义目前达到的最远位置max_bound=0，和上一步到达的边界end=0。
        2、遍历数组，遍历范围[0,n)
            a 所能达到的最远位置max_bound=max(max_bound,nums[i]+i)，表示上一最远位置和当前索引i和索引i上的步数之和中的较大者。
            b 如果索引ii到达了上一步的边界end，即i==end，则：
                更新边界end，令end等于新的最远边界max_bound，即end=max_bound
                判断可到达边界是否大于等于n-1，若满足，则返回True
        3、返回FalseFalse

    """
    def canJump(self, nums):
        max_bound = 0
        n = len(nums)
        end = 0
        for i in range(n):
            max_bound = max(max_bound, nums[i] + i)
            if i == end:
                end = max_bound
            if end >= n - 1:
                return True
        return False


class Solution2:
    """从后往前，倒序贪心"""
    def canJump(self, nums):
        lastIndex = len(nums) - 1
        for i in range(lastIndex, -1, -1):
            # 若当前位置可到达的边界大于等于lastIndex，说明lastIndex更新到当前位置
            if i + nums[i] >= lastIndex:
                lastIndex = i
        return lastIndex == 0

