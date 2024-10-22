#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
import string
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        for i in string.ascii_lowercase:
            d[i]=-1
        ans = -1
        for i in range(len(s)):
            if d[s[i]]!=-1:
                print(s[i])
                ans = max(ans, i-d[s])
                d[s[i]] = 
            else:
                d[s[i]]=i
        if ans==-1:
            return len(s)
        return ans
                
            
a=Solution()
print(a.lengthOfLongestSubstring("abcabcbb")) 
# @lc code=end

