#
# @lc app=leetcode id=1109 lang=python3
#
# [1109] Corporate Flight Bookings
#
# from typing import List
# @lc code=start
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0]* n
        for i in range(len(bookings)):
            ans[bookings[i][0]-1] += bookings[i][2]
            if bookings[i][1]<n: ans[bookings[i][1]] -= bookings[i][2]
        for i in range(1, len(ans)):
            ans[i] +=ans[i-1]
        return ans
            
            
            
        
# @lc code=end

