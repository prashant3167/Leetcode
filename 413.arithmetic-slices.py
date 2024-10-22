#
# @lc app=leetcode id=413 lang=python3
#
# [413] Arithmetic Slices
#

# @lc code=start
from typing import List
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        lc = [0]*len(nums)
        for i in range(2, len(nums)):
            if 2 * nums[i-1] == nums[i-2] + nums[i]:
                lc[i] = 1
                if i>2 and nums[i-2]-nums[i-3]==nums[i-1]-nums[i-2]:
                    lc[i] +=lc[i-1]
        print(lc)
        return sum(lc)
    # def __init__(self):
    #     pass


s=Solution()
print(s.numberOfArithmeticSlices(nums = [1,2,1,2,4,1,5,10]))
                    
                    
                
        
# @lc code=end

