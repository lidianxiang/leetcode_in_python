"""

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4
"""


class Solution:
    def singleNumber(self, nums):
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]


class Solution2:
    def singleNumber(self, nums):
        """
        数学方法：2*(a+b+c)−(a+a+b+b+c)=c
        :param nums:
        :return:
        """
        return 2 * sum(set(nums)) - sum(nums)


class Solution3:
    def singleNumber(self, nums):
        """
        异或概念

        如果我们对 0 和二进制位做 XOR 运算，得到的仍然是这个二进制位
        a \oplus 0 = aa⊕0=a
        如果我们对相同的二进制位做 XOR 运算，返回的结果是 0
        a \oplus a = 0a⊕a=0
        XOR 满足交换律和结合律
        a \oplus b \oplus a = (a \oplus a) \oplus b = 0 \oplus b = ba⊕b⊕a=(a⊕a)⊕b=0⊕b=b
        所以我们只需要将所有的数进行 XOR 操作，得到那个唯一的数字。


        :param nums:
        :return: 
        """
        a = 0
        for i in nums:
            a ^= i
        return a
