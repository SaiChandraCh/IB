class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        rows = [[False for i in range(9)] for j in range(9)]
        cols = [[False for i in range(9)] for j in range(9)]
        grids = [[False for i in range(9)] for j in range(9)]

        for i in range(9):
            for j in range(9):
                if A[i][j] == '.':
                    continue
                num = int(A[i][j]) - 1
                grid = (i // 3) * 3 + (j // 3)
                if rows[i][num] or cols[j][num] or grids[grid][num]:
                    return 0
                else:
                    rows[i][num], cols[j][num], grids[grid][num] = True, True, True

        return 1

if __name__ == '__main__':
    A = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
    ]
    print(Solution.isValidSudoku(Solution,A))