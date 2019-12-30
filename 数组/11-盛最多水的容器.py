"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

示例:

输入: [1,8,6,2,5,4,8,3,7]
输出: 49
"""


class Solution:
    """双指针法
    设置双指针i,j分别位于容器壁的两端，根据规则移动指针，并且更新面积最大值res，直到
    i == j时返回res
    """
    def maxArea(self, height):
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            # 这里要判断height[i]与height[j]的值大小，因为是以最短的那个板为基准
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res
