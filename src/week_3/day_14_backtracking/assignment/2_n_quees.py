import copy
class Solution:
    # @param A : integer
    # @return a list of list of strings
    res = []
    def __init__(self):
        Solution.res = []

    def solveNQueens(self, A):
        board = ["."*A]*A
        Solution.util(Solution, A, board, 0,0)
        print(Solution.res)

    def util(self, A, board, row,column):
        if row > A:
            return
        if row == A and board[row-1][column] == "Q":
            Solution.res.append(copy.deepcopy(board))
            return
        for column in range(A):
            if Solution.isValid(Solution, board,row,column,A):
                board[row] = board[row][:column]+"Q"+board[row][column+1:]
                Solution.util(Solution, A, board, row+1,column)
                board[row] = board[row][:column]+"."+board[row][column+1:]

    def isValid(self,board,row,column,A):
        row_temp, col_temp = row, column

        while row_temp>=0:
            # print(row_temp, col_temp)
            if board[row_temp][col_temp] != "Q":
                row_temp -= 1
            else:
                return False

        row_temp = row
        while row_temp>=0 and col_temp >= 0:
            # print(row_temp, col_temp)
            if board[row_temp][col_temp] != "Q":
                row_temp -= 1
                col_temp -= 1
            else:
                return False

        row_temp = row
        col_temp = column
        while row_temp>=0 and col_temp < A:
            # print(row_temp, col_temp)
            if board[row_temp][col_temp] != "Q":
                row_temp -= 1
                col_temp += 1
            else:
                return False
        return True

if __name__ == '__main__':
    Solution.solveNQueens(Solution,5)
    # [
    #     [".Q..", "...Q", "Q...", "..Q."],
    #
    #     ["..Q.", "Q...", "...Q", ".Q.."]
    # ]