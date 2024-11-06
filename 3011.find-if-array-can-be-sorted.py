#
# @lc app=leetcode id=3011 lang=python3
#
# [3011] Find if Array Can Be Sorted
#

# @lc code=start
import functools

def compare(x, y):
    x_bin, y_bin = bin(x), bin(y)
    # print(sum([1 for i in x_bin if i=='1']), sum([1 for i in y_bin if i=='1']))
    if sum([1 for i in x_bin if i=='1'])!=sum([1 for i in y_bin if i=='1']):
        return 0
    return x-y

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        nums = sorted(nums, key=functools.cmp_to_key(compare))
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                return False
        return True

        
# @lc code=end

