class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        m = len(A)
        n = len(A[0])
        for i in range(m):
            temp = 0
            for j in range(n-1,-1,-1):
                temp += A[i][j]
                A[i][j] = temp

        for j in range(n):
            temp = 0
            for i in range(m-1,-1,-1):
                temp += A[i][j]
                A[i][j] = temp
        max = A[0][0]
        for i in range(m):
            for j in range(n):
                if A[i][j] > max:
                    max = A[i][j]

        return max