"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    """双指针 + 排序"""
    def threeSum(self, nums):
        n = len(nums)
        res = []
        # 特殊条件：当nums不存在或是nums的长度小于3的情况，直接返回空列表
        if not nums or n < 3:
            return []
        # 对nums进行排序
        nums.sort()
        # 遍历nums数组
        for i in range(n):
            # 当遍历到的数组数已经开始大于0的情形时，就可以跳出循环了，直接返回答案了
            if nums[i] > 0:
                return res
            # 对于重复数组，跳过，避免出现重复接
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 左指针
            L = i + 1
            # 右指针
            R = n - 1
            # 当左指针小于右指针的情形
            while L < R:
                # 当三个数的和为0，以列表形式返回这三个数
                if nums[i] + nums[L] + nums[R] == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    # 当左指针出现重复项时，跳过
                    while L < R and nums[L] == nums[L+1]:
                        L += 1
                    # 当右指针出现重复项时，跳过
                    while L < R and nums[R] == nums[R-1]:
                        R -= 1
                    L += 1
                    R -= 1
                # 当三者之和大于0时，说明nums[R]的数值太大
                elif nums[i] + nums[L] + nums[R] > 0:
                    R -= 1
                # 当三者之和小于0时，说明nums[L]的数值太小
                else:
                    L += 1
        return res
