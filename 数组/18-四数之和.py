"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution:
    """排序 + 双指针"""
    def fourSum(self, nums, target):
        # 排序
        nums.sort()
        n = len(nums)

        res = []
        if n > 3:
            # 最后也是最大的两个数之和
            last_two = nums[-1] + nums[-2]
            # 最后也是最大的三个数之和
            last_three = last_two + nums[-3]
        # 第一个for循环遍历
        for i in range(n - 3):
            # 当出现相同数字的时候，直接跳过
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 定义第一变量
            num1 = nums[i]
            # 当排序后的连续四个数之和大于零的时候，就停止
            if num1 + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            # 当num1 与最后的三个数（也是最大的三个数之和）相加之和小于target，则继续（说明num1小了）
            if num1 + last_three < target:
                continue
            # 第二个for循环遍历
            for j in range(i + 1, n - 2):
                # 当j存在且出现重复的相同数字时，跳过
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # 定义第二个变量
                num2 = nums[j]
                # 当第一变量 + 第二变量 + 两个数之和大于target时就停止
                if num1 + num2 + nums[j + 1] + nums[j + 2] > target:
                    break
                # 若num1 + num2 + 最后两个数之和小于target时，则说明num1 + num2之和小了，继续循环
                if num1 + num2 + last_two < target:
                    continue
                # 再来定义两个变量k和l，使得k从j+1开始，逐渐变大，使得l重n-1开始，逐渐变小
                k = j + 1
                l = n - 1
                # 循环
                while k < l:
                    total_num = num1 + num2 + nums[k] + nums[l]
                    # 当四数之和等于target的情况，需要去掉重复元素
                    if total_num == target:
                        res.append([num1, num2, nums[k], nums[l]])
                        k += 1
                        # 当k出现重复相同的数时，跳过
                        while nums[k] == nums[k - 1] and k < l:
                            k += 1
                        l -= 1
                        # 当l出现重复相同的数时，跳过
                        while nums[l] == nums[l + 1] and k < l:
                            l -= 1
                    # 当四数之和大于target的情况
                    elif total_num > target:
                        l -= 1
                        # 当出现重复的情况
                        while nums[l] == nums[l + 1] and k < l:
                            l -= 1
                    # 当四数之和小于target的情况
                    else:
                        k += 1
                        # 当出现重复的情况
                        while nums[k] == nums[k - 1] and k < l:
                            k += 1
        return res
