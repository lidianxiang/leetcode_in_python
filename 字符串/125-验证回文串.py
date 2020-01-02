"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false
"""


class Solution:
    """双指针，一个从头开始，一个从尾开始，同时往中间移动"""

    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            # 当左指针与右指针指向的元素同时为数字或字母的话
            if s[l].isalnum() and s[r].isalnum():
                # 将字符大写进行比较
                if s[l].upper() == s[r].upper():
                    # 左指针加一，往后移动
                    l += 1
                    # 右指针减一，往前移动
                    r -= 1
                else:
                    return False
            else:
                # 当左指针指向的元素不为数字或字母
                if not s[l].isalnum():
                    l += 1
                # 当右指针指向的元素不为数字或是字母
                if not s[r].isalnum():
                    r -= 1
        return True


class Solution2:
    """
    中心扩散法，在每个字符串中插入一个特殊字符，使其变成奇数，找到中点，用两个指针同时从中点往两边移动，逐个判断字符
    """

    def isPalindrome(self, s):
        strings = '#'
        for c in s:
            if c.isalnum():
                strings += c + '#'
        # 字符串的中点
        mid = len(strings) >> 1
        l, r = mid - 1, mid + 1
        while l >= 0 and r < len(strings):
            if strings[l].upper() == strings[r].upper():
                l -= 1
                r += 1
            else:
                return False
        return True
