#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack)!=0 and val<self.min_stack[-1] :
            self.min_stack.append(val)
        else:
            if len(self.min_stack)==0:
                self.min_stack.append(val)
            else:
                 self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        if len(self.stack)!=0:
            self.min_stack.pop()
            self.stack.pop()
            
        

    def top(self) -> int:
        if len(self.stack)!=0:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        if len(self.min_stack)!=0:
            return self.min_stack[-1]
        return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

