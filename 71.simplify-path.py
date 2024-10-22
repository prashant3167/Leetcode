#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        d = path.split("/")
        if d[-1]=="":
            d.pop()
        for i in d:
            if i=="":
                continue
            if i=="..":
                if len(stack)!=0:
                    stack.pop()
            elif i==".":
                pass
            else:
                stack.append(i)
        # print(stack)
        return "/"+"/".join(stack)

# a = Solution()
# # print(a.simplifyPath("/home/user/Documents/../Pictures"))  
# @lc code=end

