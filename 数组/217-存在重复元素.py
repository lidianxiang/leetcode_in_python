"""
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

"""


class Solution:
    """利用set()来判定"""
    def containsDuplicate(self, nums):
        # 边界条件判定
        if not nums:
            return False
        elif len(nums) != len(set(nums)):
            return True
        else:
            return False


class Solution2:
    """利用排序来解决"""
    def containsDuplicate(self, nums):
        if not nums:
            return False

        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


class Solution3:
    """哈希"""
    def containsDuplicate(self, nums):
        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        return False
