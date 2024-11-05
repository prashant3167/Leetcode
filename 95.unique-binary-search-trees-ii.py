#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#


# @lc code=start
# Definition for a binary tree node.
# The code snippet you provided is defining a TreeNode class for a binary tree. This class has three
# attributes: `val` to store the value of the node, `left` to store the reference to the left child
# node, and `right` to store the reference to the right child node. The `__init__` method is the
# constructor that initializes these attributes with default values if not provided during object
# creation.
# # The TreeNode class is defined with attributes for value, left child, and right child.
# The TreeNode class represents a node in a binary tree structure.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from typing import List, Optional
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        memo = {}

        def generate_trees(start, end):
            if (start, end) in memo:
                return memo[(start, end)]

            trees = []
            if start > end:
                trees.append(None)
                return trees

            for root_val in range(start, end + 1):
                left_trees = generate_trees(start, root_val - 1)
                right_trees = generate_trees(root_val + 1, end)

                for left_tree in left_trees:
                    for right_tree in right_trees:
                        root = TreeNode(root_val, left_tree, right_tree)
                        trees.append(root)

            memo[(start, end)] = trees
            return trees

        return generate_trees(1, n)


# @lc code=end
