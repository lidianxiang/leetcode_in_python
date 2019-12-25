"""
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false

"""


class Solution:
    """哈希"""

    def containsNearbyDuplicate(self, nums, k):
        # d = dict()来创建字典比使用 d = {}速度更快点，所以尽量使用前者来创建字典
        hash = dict()
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]] = i
            else:
                if i - hash[nums[i]] <= k:
                    return True
                else:
                    hash[nums[i]] = i
        return False


class Solution2:
    """哈希，但是用到了python自带的enumerate()函数，速度更快点"""
    def containsNearbyDuplicate(self, nums, k):
        # d = dict()来创建字典比使用 d = {}速度更快点，所以尽量使用前者来创建字典
        d = dict()
        for i, num in enumerate(nums):
            if num in d:
                if i - d[num] <= k:
                    return True
            d[num] = i
        return False

