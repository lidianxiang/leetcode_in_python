"""
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""


class Solution:
    def merge(self, intervals):
        # 根据区间的开始排序
        intervals.sort(key=lambda x: x[0])
        # 创建保存最后结果的列表
        merged = []
        # 遍历二维数组
        for interval in intervals:
            # 当每个区间还没比较或是保存列表的结束点小于区间的开始节点，表示两者并未存在重复区间
            if not merged or merged[-1][-1] < interval[0]:
                merged.append(interval)
            else:
                # 否则即存在重复区间，并取两者的最大值为结束点
                merged[-1][1] = max(merged[-1][-1], interval[-1])
        return merged
