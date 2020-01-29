"""
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
"""


class Solution:
    """使用hash表来存储之前的信息，避免重复存储之前的数字"""
    def subarraySum(self, nums, k):
        # 这里字典的key表示前i个值的和，value表示出现的key的次数
        prefixSumArray = {0: 1}
        count = 0
        prefixSum = 0
        for num in nums:
            prefixSum += num
            subArray = prefixSum - k
            if subArray in prefixSumArray:
                count += prefixSumArray[subArray]
            # 当subArray不在dict中，vaule加一，更新hash表
            # python中字典中的get(key, default=None)函数,dict中有key，则取出key对应的value，否则设置为default值，此处表示为0
            prefixSumArray[prefixSum] = prefixSumArray.get(prefixSum, 0) + 1
        return count
