class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        temp = [0 for _ in range(A)]
        result = [ temp for _ in range(A)]
        i = 0
        j = 0
        visited_row = 0
        visited_col = 0
        for val in range(1,(A*A)+1):
            result[i][j] = val

        return result

if __name__ == '__main__':
    print(Solution.generateMatrix(Solution,5))