"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
"""


class Solution:
    """DP
    难点在于：在一个位置能容下的雨水量等于它左右两边柱子最大高度的最小值减去它的高度。
    """
    def trap(self, height):
        if not height:
            return 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        max_left[0] = height[0]
        max_right[-1] = height[-1]
        for i in range(1, n):
            # 左边柱子的高度
            max_left[i] = max(height[i], max_left[i-1])
        for i in range(n-2, -1, -1):
            # 右边柱子的高度
            max_right[i] = max(height[i], max_right[i+1])
        # 结果
        res = 0
        for i in range(n):
            # 结果等于左右两边柱子的较小值减去它的高度
            res += min(max_left[i], max_right[i]) - height[i]
        return res


class Solution2:
    """双指针解法"""
    def trap(self, height):
        # 特判
        if not height:
            return 0
        # 左右指针
        left, right = 0, len(height) - 1
        res = 0
        # 记录左右边最大值
        left_max = height[left]
        right_max = height[right]
        # 遍历数组
        while left < right:
            # 当左边高度小于右边高度
            if height[left] < height[right]:
                if left_max > height[left]:
                    res += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            # 当右边高度小于左边高度
            else:
                if right_max > height[right]:
                    res += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1
        return res


class Solution3:
    """栈"""
    def trap(self, height):
        # 特判
        if not height:
            return 0

        n = len(height)
        stack = []
        res = 0
        for i in range(n):
            while stack and height[stack[-1]] < height[i]:
                tmp = stack.pop()
                if not stack:
                    break
                res += (min(height[i], height[stack[-1]]) - height[tmp]) * (i - stack[-1] - 1)
            stack.append(i)
        return res
