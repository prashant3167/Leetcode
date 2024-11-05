#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def inOrder(node):
            if not node or self.stop:
                return
            
            inOrder(node.left)
            
            if self.prev and self.prev.val > node.val:
                if self.a:
                    self.b = node
                    self.stop = True
                else:
                    self.a = self.prev
                    self.b = node
            
            self.prev = node
            
            inOrder(node.right)
        
        self.prev = None
        self.a = self.b = None
        self.stop = False
        
        inOrder(root)
        self.a.val, self.b.val = self.b.val, self.a.val
        
        return
        
# @lc code=end

