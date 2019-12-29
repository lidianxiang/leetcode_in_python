"""
给定一个长度为 n 的整数数组，你的任务是判断在最多改变 1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中所有的 i (1 <= i < n)，满足 array[i] <= array[i + 1]。

示例 1:

输入: [4,2,3]
输出: True
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
示例 2:

输入: [4,2,1]
输出: False
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
说明:  n 的范围为 [1, 10,000]。

"""


class Solution:
    """
    对nums数组复制两份a1，a2。对一份改大，对另外一份改小，且只改动一次。
    然后对a1和排序后的a1进行比较，对a2和排序后的a2进行比较。只要其中一个
    是相等的，即返回True
    """
    def checkPossibility(self, nums):
        if len(nums) <= 2:
            return True
        a1 = nums[:]
        a2 = nums[:]
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                a1[i+1] = nums[i]
                a2[i] = nums[i+1]
                break
        return a1 == sorted(a1) or a2 == sorted(a2)


class Solution2:
    """
    设置计数器count=0。从i=1到i=nums.size()遍历nums。nums[i-1]>nums[i]时，
    修改数组不外乎有两种情况，使其中大的变成跟小的一样，或者使其小的变成跟大的一样。
    变大无所谓，对前面的顺序不会发生影响。但变小的话，容易对前面的序列发生影响，
    比如nus[i-2]>nums[i]，这样的话，如果是这种情况，或者i==1，则进行改小，其余的情况都进行改大。
    当count大于2时，直接返回false。否则为true。
    """
    def checkPossibility(self, nums):
        if len(nums) <= 2:
            return True

        count = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                count += 1
                if i == 1 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
                if count > 1:
                    return False
        return True
