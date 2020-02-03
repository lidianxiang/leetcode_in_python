"""
验证给定的字符串是否可以解释为十进制数字。

例如:

"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。这里给出一份可能存在于有效十进制数字中的字符列表：

数字 0-9
指数 - "e"
正/负号 - "+"/"-"
小数点 - "."
"""


class Solution:
    """
    正则表达式：
            1、前面的符号：[\+\-]?
            2、e前面的数字（13。14）：(\d+\.\d+|\.\d+|\d+\.|\d+)-->分了4种情况：0.0, .0,0.,0
            3、e及其指数（e-520）：(e[\+\-]?\d+)
    """
    def isNumber(self, s: str) -> bool:
        import re
        pattern = re.compile(r"^[\+\-]?(\d+\.\d+|\.\d+|\d+\.|\d+)(e[\+\-]?\d+)?$")
        return True if len(re.findall(pattern, s.strip())) else False
