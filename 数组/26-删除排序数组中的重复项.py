"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。

"""


class Solution:
    """
    看了一些大佬的解题思路, 大多数都是考虑使用双指针从头到尾遍历.
    这样用for循环就会衍生出一个问题: 在遍历列表/数组/切片等的过程中, 此时该列表/数组/切片等的长度会发生变化.
    然后有很多大佬直接改用while循环进行解答.

    其实, 我们可以换位思考一下: 正向遍历有影响, 我可以反向遍历啊. 想到这个, 题目就很好解了.

    1、从nums的最后一个开始遍历, 然后与前一个进行对比.
    2、如果相等, 则删除该位置的数.
    3、不等, 则继续往前遍历.

    """
    def removeDuplicates(self, nums):
        for num_index in range(len(nums)-1, 0, -1):
            if nums[num_index] == nums[num_index - 1]:
                nums.pop(num_index)

        return len(nums)


class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 定义两个指针pre,cur
        pre, cur = 0, 1
        # 遍历数组
        while cur < len(nums):
            # 当两个指针所指的数组值相等时
            if nums[pre] == nums[cur]:
                # pop掉cur指针所指的值
                nums.pop(cur)
            else:
                # 不等时，pre指针和cur指针各向前进一位
                pre, cur = pre + 1, cur + 1
        # 返回最后数组的长度
        return len(nums)
