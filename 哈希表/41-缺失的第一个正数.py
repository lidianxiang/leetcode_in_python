"""
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:

输入: [1,2,0]
输出: 3
示例 2:

输入: [3,4,-1,1]
输出: 2
示例 3:

输入: [7,8,9,11,12]
输出: 1
"""


class Solution:
    """利用哈希思想，将索引作为哈希表"""
    def firstMissingPositive(self, nums):
        n = len(nums)
        # 数字1是否存在在数组中，不存在则返回1
        if 1 not in nums:
            return 1
        # 如果nums = [1]，则返回2
        if n == 1:
            return 2
        # 当数组中存在负数和大于n的数字，替换为1
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        # 遍历数组，当读到数字a时，替换第a个元素的符号
        for i in range(n):
            a = abs(nums[i])
            if a == n:
                nums[0] = -abs(nums[0])
            else:
                nums[a] = -abs(nums[a])
        # 再次遍历数组， 返回第一个正数元素的下标
        for i in range(1, n):
            if nums[i] > 0:
                return i

        if nums[0] > 0:
            return n
        # 如果之前的步骤中都没有发现nums中的正数元素则返回n+1
        return n + 1
