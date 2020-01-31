"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution:
    """回溯算法"""
    def combinationSum(self, candidates, target):
        size = len(candidates)
        # 特判
        if size == 0:
            return []
        # 排序加速运算
        # 剪枝的前提是数组元素排序
        candidates.sort()
        # 在遍历的过程中记录路径，一般而言它是一个栈
        path = []
        res = []
        # 注意要传入size，在range中，size取不到
        self._dfs(candidates, 0, size, path, res, target)
        return res

    def _dfs(self, candidates, begin, size, path, res, target):
        # 先写递归终止情况
        if target == 0:
            # python中可变对象是引用传递，因此需要将当前path里的值拷贝出来
            # 或者使用path.copy()
            res.append(path[:])
        for index in range(begin, size):
            residue = target - candidates[index]
            # 剪枝操作，不必递归到下一层，并且后面的分枝也不必执行
            if residue < 0:
                break
            path.append(candidates[index])
            # 因为下一层不能比上一层还小，起始索引还从index开始
            self._dfs(candidates, index, size, path, res, residue)
            path.pop()
