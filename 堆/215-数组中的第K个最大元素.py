"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
"""


class Solution:
    """排序"""
    def findKthLargest(self, nums, k):
        nums.sort(reverse=True)
        return nums[k-1]


class Solution2:
    """利用python自带的堆工具"""
    def findKthLargest(self, nums, k):
        import heapq
        # print(heapq.nlargest(k, nums))
        return heapq.nlargest(k, nums)[-1]


class Solution3:
    """
    自建堆
    """
    def findKthLargest(self, nums, k):
        def adjust_heap(idx, max_len):
            left = 2 * idx + 1
            right = 2 * idx + 2
            max_loc = idx
            if left < max_len and nums[max_loc] < nums[left]:
                max_loc = left
            if right < max_len and nums[max_loc] < nums[right]:
                max_loc = right
            if max_loc != idx:
                nums[idx], nums[max_loc] = nums[max_loc], nums[idx]
                adjust_heap(max_loc, max_len)

        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            adjust_heap(i, n)
        res = None
        for i in range(1, k + 1):
            res = nums[0]
            nums[0], nums[-i] = nums[-i], nums[0]
            adjust_heap(0, n - i)
        return res


class Solution4:
    """快排"""
    def findKthLargest(self, nums, k):
        def partition(left, right):
            pivot = nums[left]
            l = left + 1
            r = right
            while l <= r:
                # if nums[l] < pivot and nums[r] > pivot:
                if nums[l] < pivot < nums[r]:
                    nums[l], nums[r] = nums[r], nums[l]
                if nums[l] >= pivot:
                    l += 1
                if nums[r] <= pivot:
                    r -= 1
            nums[r], nums[left] = nums[left], nums[r]
            return r

        left = 0
        right = len(nums) - 1
        while 1:
            idx = partition(left, right)
            if idx == k - 1:
                return nums[idx]
            if idx < k - 1:
                left = idx + 1
            if idx > k - 1:
                right = idx - 1
