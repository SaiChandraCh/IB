class Solution:
    pascal_triangle = []
    def generate(self, numRows):
        for i in range(numRows):
            Solution.pascal_triangle.append([1 for _ in range(i+1)])
        print(Solution.pascal_triangle)
        self.util(self,total_rows = numRows,curr_row=2,column=1)

    def util(self, total_rows, curr_row, column):
        if total_rows == curr_row:
            return
        if curr_row == column:
            self.util(self, total_rows, curr_row+1, 1)
            return
        Solution.pascal_triangle[curr_row][column] = Solution.pascal_triangle[curr_row-1][column-1] + Solution.pascal_triangle[curr_row-1][column]
        self.util(self,total_rows,curr_row,column+1)

if __name__ == '__main__':
    Solution.generate(Solution,6)