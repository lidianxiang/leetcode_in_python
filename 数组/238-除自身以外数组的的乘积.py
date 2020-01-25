"""
给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
"""


class Solution:
    """
    1、初始化两个空数组 L 和 R。对于给定索引 i，L[i] 代表的是 i 左侧所有数字的乘积，R[i] 代表的是 i 右侧所有数字的乘积。
    2、我们需要用两个循环来填充 L 和 R 数组的值。对于数组 L，L[0] 应该是 1，因为第一个元素的左边没有元素。对于其他元素：L[i]=L[i-1]*nums[i-1]。
    3、同理，对于数组 R，R[length-1] 应为 1。length 指的是输入数组的大小。其他元素：R[i]=R[i+1]*nums[i+1]。
    4、当 R 和 L 数组填充完成，我们只需要在输入数组上迭代，且索引 i 处的值为：L[i]*R[i]。
    """
    def productExceptSelf(self, nums):
        length = len(nums)
        L, R, answer = [0] * length, [0] * length, [0] * length
        L[0] = 1
        for i in range(1, length):
            L[i] = nums[i - 1] * L[i - 1]
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            R[i] = nums[i + 1] * R[i + 1]

        for i in range(length):
            answer[i] = L[i] * R[i]
        return answer


class Solution2:
    """
    1、初始化 answer 数组，对于给定索引 i，answer[i] 代表的是 i 左侧所有数字的乘积。
    2、构造方式与之前相同，只是我们试图节省空间。
    3、这种方法的唯一变化就是我们没有构造 R 数组。而是用一个遍历来跟踪右边元素的乘积。
       并更新数组 answer[i]=answer[i]*R。
       然后R更新为 R=R*nums[i]
    """
    def productExceptSelf(self, nums):
        length = len(nums)
        answer = [0] * length
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]

        R = 1
        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i]
        return answer
