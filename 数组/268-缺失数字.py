"""
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

示例 1:

输入: [3,0,1]
输出: 2
示例 2:

输入: [9,6,4,2,3,5,7,0,1]
输出: 8

"""


class Solution:
    """排序"""
    def missingNumber(self, nums):
        # 数组排序
        nums.sort()
        # 判断边界条件
        if nums[-1] != len(nums):
            return len(nums)
        # 判断边界条件
        if nums[0] != 0:
            return 0
        # 遍历数组
        for i in range(1, len(nums)):
            expected_num = nums[i - 1] + 1
            if nums[i] != expected_num:
                return expected_num


class Solution2:
    """
    哈希表
    思路：我们可以直接查询每个数是否在数组中出现过来找出缺失的数字。
         如果使用哈希表，那么每一次查询操作都是常数时间的。
    """
    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number


class Solution3:
    """
    异或运算（XOR）
    思路：由于异或运算（XOR）满足结合律，并且对一个数进行两次完全相同的异或运算会得到原来的数，
         因此我们可以通过异或运算找到缺失的数字。
    """
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing


class Solution4:
    """
    高斯求和公式
    思路：我们在线性时间内可以求出数组中所有数的和，
    并在常数时间内求出前n+1 个自然数（包括 0）的和，将后者减去前者，就得到了缺失的数字。
    """
    def missingNumber(self, nums):
        expected_sum = len(nums) * (len(nums) + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
