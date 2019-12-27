"""
假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。

示例 1:

输入: flowerbed = [1,0,0,0,1], n = 1
输出: True
示例 2:

输入: flowerbed = [1,0,0,0,1], n = 2
输出: False
"""


class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        limit = 0
        # 前后补0
        add_flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(add_flowerbed) - 1):
            # 如果连续三个全是零的话，就可以种下一颗树
            if sum(add_flowerbed[i-1:i+2]) == 0:
                # 如果可以，种下一棵树
                add_flowerbed[i] = 1
                limit += 1
        # 判断两者大小来决定是否可以种得下
        return limit >= n
