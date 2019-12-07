"""
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:

输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]

"""


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
        return [i + 1 for i, num in enumerate(nums) if num > 0]


class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 创建一个从1到n的集合，这里加一的原因是range()函数不包括第二个参数，所以要加一
        length = len(nums) + 1
        # 创建a集合
        a = set([i for i in range(1, length)])
        # 将列表nums转化成集合nums
        b = set(nums)
        # 求集合a和集合b的差集
        return list(a - b)
