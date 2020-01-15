'''
外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1"（"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。

注意：整数序列中的每一项将表示为一个字符串。

 

示例 1:

输入: 1
输出: "1"
解释：这是一个基本样例。
示例 2:

输入: 4
输出: "1211"
解释：当 n = 3 时，序列是 "21"，其中我们有 "2" 和 "1" 两组，"2" 可以读作 "12"，也就是出现频次 = 1 而 值 = 2；类似 "1" 可以读作 "11"。所以答案是 "12" 和 "11" 组合在一起，也就是 "1211"。

'''


class Solution:
    """递归"""
    def countAndSay(self, n):
        if n == 1:
            return '1'
        # 关键点，在字符串末尾拼接时，要加上一个非1-3的数字
        num = self.countAndSay(n-1) + '*'
        # print(num)
        # 字符串转列表
        temp = list(num)
        count = 1
        strBulider = ''
        for i in range(len(temp)-1):
            # 当第i个数字和第i+1个字符相同时，count加一
            if temp[i] == temp[i+1]:
                count += 1
            # 当第i个数字和第i+1个字符不相同时
            else:
                # 记录当前的count值和当前字符
                strBulider += str(count) + temp[i]
                # 令count重新置1
                count = 1
        return strBulider


class Solution2:
    """非递归版"""
    def countAndSay(self, n):
        # 初始
        prev_person = '1'
        # 外循环
        for i in range(1, n):
            next_person, num, count = '', prev_person[0], 1
            #内循环
            for j in range(1, len(prev_person)):
                # 前一字符与当前字符相同时，count加一
                if prev_person[j] == num:
                    count += 1
                else:
                    # 记录count与字符
                    next_person += str(count) + num
                    # 更新num值
                    num = prev_person[j]
                    # count置一
                    count = 1
            next_person += str(count) + num
            prev_person = next_person
        return prev_person
