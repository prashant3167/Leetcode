#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxlen = L = 0
        for R in range(len(nums)):
            if nums[R] == 0: k -= 1

            while k < 0: 
                if nums[L] == 0: 
                   k += 1
                L += 1
            maxlen = max(maxlen, R - L + 1)
            
        return maxlen



# nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# k = 3
# a=Solution()
# print(a.longestOnes(nums=nums, k=k))
# @lc code=end

