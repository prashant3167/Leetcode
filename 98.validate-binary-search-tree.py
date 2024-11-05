#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def min_tree(root):
    #     if root.left==None or root.right==None:
    #         return (root.left)
    def isValidBST_utils(self, root: Optional[TreeNode]):
        if root==None:
            return (True, None, None)
        
        validl, mal, mil = self.isValidBST_utils(root.left)
        validr, mar, mir = self.isValidBST_utils(root.right)
        # print("l",root.val, validl, mal, mil)
        # print("r",root.val, validr, mar, mir)
        valid = validl and validr
        if mal!=None and mal>=root.val:
            valid = False
        if mir!=None and mir<=root.val:
            valid = False
        # print(root.val, max(mal if mal!=None else root.val, root.val), min(mir if mir!=None else root.val, root.val))
        return (valid, max(mar if mar!=None else root.val, root.val), min(mil if mil!=None else root.val, root.val))
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        x, _, _ = self.isValidBST_utils(root)
        return x
        
        
# @lc code=end


[5,4,6,null,null,3,7]
