#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        ans = [0]*(n+1)
        ans[1] = 1
        ans[2] = 2
        for i in range(3, n+1):
            # print(i)
            for j in range(1,i+1):
                left = j-1
                right = i-j
                ans[i] +=(max(ans[left],1)*max(ans[right],1))
        return ans[n]

# a=Solution()
# print(a.numTrees(3))
        
# @lc code=end

