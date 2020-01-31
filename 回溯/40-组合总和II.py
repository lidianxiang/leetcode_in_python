"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
"""


class Solution:
    def combinationSum2(self, candidates, target):
        # 特判
        if len(candidates) == 0:
            return []
        path = []
        res = []
        # 排序
        candidates.sort()
        self._dfs(candidates, target, 0, path, res)
        return res

    def _dfs(self, candidates, target, begin, path, res):
        path = path.copy()
        # 递归终止条件
        if target == 0:
            res.append(path)
            return

        if begin > len(candidates) - 1:
            return

        for cur in range(begin, len(candidates)):
            # 同一层级避免重复元素
            if cur > begin and candidates[cur - 1] == candidates[cur]:
                continue

            temp = target - candidates[cur]
            # 剪枝操作
            if temp < 0:
                return
            else:
                path.append(candidates[cur])
                self._dfs(candidates, temp, cur+1, path, res)
                path.pop()

