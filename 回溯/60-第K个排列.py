"""
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"
"""


class Solution:
    """回溯 + 剪枝"""
    def getPermutation(self, n, k):
        def fact(n):
            ret = 1
            while n:
                ret *= n
                n -= 1
            return ret

        def dfs(remain, path, k):
            if not remain:
                return path

            lenght = len(remain)
            # 对于每一层，该层每个分支的数量相当于剩余数量-1的阶乘
            count = fact(lenght - 1)
            for i in range(lenght):
                # 此处如果k大于该分支排列的数量，那么减去该分支
                if k > count:
                    k -= count
                else:
                    return dfs(remain[:i] + remain[i + 1:], path + remain[i], k)

        return dfs([str(i) for i in range(1, n + 1)], '', k)


class Solution2:
    """
    数学规律
    """
    def getPermutation(self, n, k):
        import math
        num = [str(i) for i in range(1, n + 1)]
        res = ""
        n -= 1
        while n > -1:
            t = math.factorial(n)
            loc = math.ceil(k / t) - 1
            res += num[loc]
            num.pop(loc)
            k %= t
            n -= 1
        return res
