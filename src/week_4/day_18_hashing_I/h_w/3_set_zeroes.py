class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        x_zero_map = {}
        y_zero_map = {}
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 0:
                    x_zero_map[i] = True
                    y_zero_map[j] = True
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i in x_zero_map or j in y_zero_map:
                    A[i][j] = 0
        return A

if __name__ == '__main__':
    A = [   [1, 0, 1],
        [1, 1, 1],
        [1, 1, 1]   ]

    Solution.setZeroes(Solution,A)