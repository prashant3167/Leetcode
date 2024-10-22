#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
# from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            if nums[i]>0:
                nums[i] = nums[i] + (nums[i-1] if i>0 and nums[i-1]>0  else 0)
                ans = max(nums[i], ans)
        return ans
                
            

# a=Solution()
# print(a.findMaxConsecutiveOnes([1,0,1,1,0,1]))
        
# @lc code=end

