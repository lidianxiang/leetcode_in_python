"""
给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。

数学表达式如下:

如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。

示例 1:

输入: [1,2,3,4,5]
输出: true
示例 2:

输入: [5,4,3,2,1]
输出: false
"""


class Solution:
    def increasingTriplet(self, nums):
        min_num, sec_num = float('inf'), float('inf')
        # 遍历数组
        for num in nums:
            min_num = min(num, min_num)
            # 当数组中的元素大于最小值，比较第二小的值
            if num > min_num:
                sec_num = min(num, sec_num)
            # 当数组中的元素大于第二小的值时，那么就存在了第三小的值，那么就返回Fale
            if num > sec_num:
                return True
        # 当遍历完数组仍然找不到第三小的元素，则返回False
        return False
