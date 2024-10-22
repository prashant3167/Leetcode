#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums)<=3:
            return max(nums)
        nums2 = nums[1:]
        for i in range(2, len(nums)-1):
        
            nums[i] +=max(nums[i-2],nums[i-3] if i>=3 else -1)
        for i in range(2, len(nums2)):
            nums2[i] +=max(nums2[i-2],nums2[i-3] if i>=3 else -1)
        
        return max(max(nums[-2], nums[-3]), max((nums2[-1], nums2[-2])))
#         def __init__(self):
#             return None
        
        
# a = Solution()
# print(a.rob([2,4,8,9,9,3]))
# print(a.rob([200,3,140,20,10]))

# print(a.rob([1,3,1,3,100]))


        
# @lc code=end

