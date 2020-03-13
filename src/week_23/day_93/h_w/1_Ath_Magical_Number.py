# class Solution:
#     # @param A : integer
#     # @param B : integer
#     # @param C : integer
#     # @return an integer
#     def solve(self, A, B, C):
#         flag = False
#         i, j = 0, 0
#         if B<C:
#             flag = True
#         res = 0
#         for K in range(A):
#             if flag:
#                 i += 1
#                 res = B*i
#             else:
#                 j += 1
#                 res = C*j
#             flag = not flag
#         print(res)
#         return res%((10**9)+7)
#
# if __name__ == '__main__':
#     print(Solution.solve(Solution, 807414236, 3788, 38141))

class Solution:
    def setZeroes(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        to_visit = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    to_visit[i] = j
        print(to_visit)
        self.util(self, matrix,1,to_visit[1])
        for i in to_visit:
            self.util(self, matrix,i,to_visit[i])
        print(matrix)

    def util(self, A, i, j):
        if i<0 or j<0 or i>len(A) or j>len(A[0]):
            return
        self.util(self, A, i-1 , j)
        self.util(self, A, i+1 , j)
        self.util(self, A, i , j-1)
        self.util(self, A, i , j+1)

if __name__ == '__main__':
    Solution.setZeroes(Solution,[[1,1,1],[1,0,1],[1,1,1]])