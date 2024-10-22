#
# @lc app=leetcode id=275 lang=python3
#
# [275] H-Index II
#

# @lc code=start
from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        ans = 0
        for i in range(len(citations)):
            # print(citations[i], i)
            if citations[i]>=i+1:
                ans = max(ans, i+1)
        # if len(citations)<=citations[-1]:
        #     return len(citations)
        return ans
        

# a = Solution()
# print(a.hIndex([1,2, 100]))
        
# @lc code=end

