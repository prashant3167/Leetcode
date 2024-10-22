#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # a=
        for i in range(2, len(nums)):
            # print("a", nums[i],nums[i-2], nums[i-3])
        
            nums[i] +=max(nums[i-2],nums[i-3] if i>=3 else -1)
            # print(nums[i])
            
        
        return max(nums[-1], nums[-2])
    
#     def __init__(self):
#         return None
        
        
# a = Solution()
# print(a.rob([1,7,9,2]))

    

            
        
# @lc code=end

