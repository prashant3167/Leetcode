#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        d = [0]*n
        d[0]=1
        d[1] = 1
        for i in range(3, n+1):
            m = i-1
            for j in range(1, i):
                m = max([m, d[i-j-1]*j, (i-j)*j, (i-j)*d[j-1]])
                # if 
            d[i-1]=m
        return d[-1]
                
    # 3-1
    

# a = Solution()
# a.integerBreak(10)
# @lc code=end

