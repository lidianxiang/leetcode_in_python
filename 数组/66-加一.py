"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

"""


class Solution:
    def plusOne(self, digits):
        # 如果空列表直接加1
        if digits == []:
            return [1]
        # 如果最后一位小于9，直接加一就行
        if digits[-1] < 9:
            return digits[:-1]+[digits[-1] + 1]
        else:
            # 否则的话，使用递归方式加一
            return self.plusOne(digits[:-1]) + [0]


class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 进位标志，同时也是加一的数
        carry = 1
        # 反向循环列表
        for i in range(len(digits), -1, -1):
            # 每个数加一
            digits[i] += 1
            # 当加一后的数还是小于10
            if digits[i] < 10:
                # 进位标志改为0
                carry = 0
                break
            else:
                # 当加一后的数大于10，则减去10，变成个位数
                digits[i] -= 10
        # 当最后时，即第一位也发生进位操作时，在最头出插入一个数字1
        if carry == 1:
            digits.insert(0, 1)
        return digits
