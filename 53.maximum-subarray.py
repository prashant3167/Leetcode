#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """AI is creating summary for maxSubArray

        Args:
            nums (List[int]): [description]

        Returns:
            int: [description]
        """
       max_ans = -1
       max_val = max(nums)
       if max_val<0:
           return max_val
       current_value = 0
       for i in range(len(nums)):
           current_value = current_value + nums[i]
           if current_value > max_ans:
               max_ans = current_value
           if current_value < 0:
               current_value = 0
       return max_ans 
               
# @lc code=end

