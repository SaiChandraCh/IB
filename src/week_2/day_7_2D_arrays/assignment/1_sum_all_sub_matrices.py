class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        sum = 0
        for i in range(N):
            for j in range(N):
                sum += (i + 1) * (j + 1) * (N - i) * (N - j) * A[i][j]

        return sum
if __name__ == '__main__':
    print(Solution.solve(Solution,[ [1,1],[1,1] ]))