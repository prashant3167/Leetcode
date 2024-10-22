#
# @lc app=leetcode id=446 lang=python3
#
# [446] Arithmetic Slices II - Subsequence
#

# @lc code=start
from typing import List
# from collections import unordered_list
from pprint import pprint
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        totalCount = 0
         # initialize a list of dictionaries to store counts of subsequences
        dp = [{} for _ in range(n)]

        for i in range(n):
            for j in range(i):
                # calculate the difference between current and previous elements
                diff = nums[i] - nums[j]

                # get the count of subsequences with the same difference ending at nums[j]
                prevCount = dp[j].get(diff, 0)
                # update count of subsequences ending at nums[i]
                dp[i][diff] = dp[i].get(diff, 0) + prevCount + 1
                # accumulate the previous count to the total count
                totalCount += prevCount

        return totalCount
    
#     def __init__(self):
#         pass

# d = Solution()
# # d.numberOfArithmeticSlices([1,2,1,2,4,1,5,10])
# print(d.numberOfArithmeticSlices([2,4,6,8,10]))
        
                
        
# @lc code=end

