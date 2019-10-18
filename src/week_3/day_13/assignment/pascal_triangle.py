class Solution:
    pascal = []
    def generate(self, numRows):
        # for i in range(numRows,0,-1):
        self.pascal(5,5)

    # def util(self, n):
    #     if n == 1:
    #         return [1]
    #     row = []
    def pascal(row, column):
        if column == 0:
            return 1
        elif row == 0:
            return 0
        else:
            return Solution.pascal(row-1, column) + Solution.pascal(row-1, column-1)

if __name__ == '__main__':
    Solution.generate(Solution,5)