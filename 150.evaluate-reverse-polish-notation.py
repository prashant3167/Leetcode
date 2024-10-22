#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i in ["+", "-", "*", "/"]:
                y, x = s.pop(), s.pop()
                s.append(int(eval(f"{x}{i}{y}")))
            else:
                s.append(i)
        return int(s[-1])
        
        
# @lc code=end

