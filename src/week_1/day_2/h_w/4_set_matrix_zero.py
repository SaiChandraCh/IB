class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        m = len(A)
        n = len(A[0])
        index_i = { i : 1 for i in range(m)}
        index_j = { i : 1 for i in range(n)}

        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    index_i[i] = 0
                    index_j[j] = 0

        print("rows => ",index_i,"cols => ",index_j)
        for i in range(m):
                for j in range(n):
                    if index_i[i] == 0 or index_j[j] == 0:
                        A[i][j] = 0

        return A

if __name__ == '__main__':
    print(Solution.setZeroes(Solution,[[1,0,1],
                                       [1,1,1],
                                       [1,1,1]]))