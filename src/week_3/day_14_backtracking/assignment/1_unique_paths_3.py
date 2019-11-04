"""
Input 1:
    A = [   [1, 0, 0, 0]
            [0, 0, 0, 0]
            [0, 0, 2, -1]   ]
Output 1:
    2
Explanation 1: We have the following two paths:
    1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
    2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Input 2:
    A = [   [0, 1]
            [2, 0]    ]
Output 2:
    0
"""

class Solution:
    # @param A : list of list of integers
    # @return an integer
    count = 0
    def __init__(self):
        Solution.count = 0

    def solve(self, A):
        if A[0][0] == 0:
            return 0
        Solution.util(self, A, x=0,y=0,rows = len(A[0]),cols = len(A))

    def util(self, grid, x, y, rows, cols):
        if grid[x][y] == -1:
            return

