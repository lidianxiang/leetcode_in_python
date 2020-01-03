"""
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]

"""

import heapq
import collections


class Solutions:
    """
    1、首先建立一个元素值对应的出现频率的哈希表，在python中有个collections库中的Counter方法可以构建我们需要的哈希表
    2、建立堆。在python中可以使用heapq库中的nlargest方法。堆中添加一个元素的复杂度是O(log(K)),要进行N次复杂度是O(N)，
    """

    def topKFrequent(self, nums, k):
        # 建立元素值与出现频率的哈希表
        count = collections.Counter(nums)
        # 构建堆，利用堆的性质来返回topK问题
        return heapq.nlargest(k, count.keys(), key=count.get)


class Solution:
    """堆排序处理海量数据的topK问题"""

    def topKFrequent(self, nums, k):
        # 对于堆的子树（parent，left_child, right_child）的交换过程，将最小值总是放在最上面
        def heapify(arr, n, i):
            smallest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and arr[l][1] < arr[i][1]:
                smallest = l
            if r < n and arr[r][1] < arr[smallest][1]:
                smallest = r
            if smallest != i:
                arr[i], arr[smallest] = arr[smallest], arr[i]
                heapify(arr, n, smallest)

        # 构建字典遍历一次统计出现频率
        map_dict = {}
        for item in nums:
            if item not in map_dict.keys():
                map_dict[item] = 1
            else:
                map_dict[item] += 1

        map_arr = list(map_dict.items())
        length = len(map_dict.keys())
        # 取前k个数，构建规模为k的最小堆
        if k <= length:
            k_minheap = map_arr[:k]
            for i in range(k // 2 - 1, -1, -1):
                heapify(k_minheap, k, i)
            for i in range(k, length):
                if map_arr[i][1] > k_minheap[0][1]:
                    k_minheap[0] = map_arr[i]
                    heapify(k_minheap, k, 0)
        # 遍历规模k之外的数据，大于堆顶则入堆，维护规模为k的最小堆
        for i in range(k - 1, 0, -1):
            k_minheap[i], k_minheap[0] = k_minheap[0], k_minheap[i]
            k -= 1
            heapify(k_minheap, k, 0)
        return [item[0] for item in k_minheap]
