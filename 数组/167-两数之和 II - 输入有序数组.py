"""
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

"""


class Solution:
    """
    双指针
    让指针i,j分别指向数组首尾，计算numbers[i]+numbers[j]，
    若两数之和大于目标，则说明此时的j和所有可用数相加都大于target，也即t于结果无用，此时应将这个数剔除，
    将j减1实现这一目的；反之，应将i+1。如此重复，直至找到结果。
    """
    def twoSum(self, numbers, target):
        n = len(numbers)
        i, j = 0, n-1
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i+1, j+1]
