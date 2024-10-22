#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        col = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    row.add(r)
                    col.add(c)
        for r in row:
            for c in range(len(matrix[0])):
                matrix[r][c] = 0
        for c in col:
            for r in set(range(len(matrix)))-row:
                matrix[r][c] = 0
        return matrix
                
        
# @lc code=end

